#!/usr/bin/env python3
"""Exact algebraic fixtures for the vacuum-refinement continuation.

Run with Python 3 and SymPy: python verify.py --output verification.json
These fixtures do not compute an interacting Yang--Mills vacuum or prove
any continuum analytic statement. Those proofs are in RESEARCH_NOTE.md.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import sympy as sp

CHECKS: list[str] = []


def equal(name: str, left, right=0) -> None:
    delta = left - right
    values = list(delta) if isinstance(delta, sp.MatrixBase) else [delta]
    if any(sp.simplify(value) != 0 for value in values):
        raise AssertionError(f"{name}: nonzero residual {delta}")
    CHECKS.append(name)


def positive(name: str, matrix: sp.MatrixBase) -> None:
    equal(name + ': Hermitian', matrix, matrix.conjugate().T)
    # All principal minors characterize a Hermitian positive semidefinite matrix.
    for length in range(1, matrix.rows + 1):
        for indices in itertools.combinations(range(matrix.rows), length):
            determinant = sp.factor(matrix.extract(indices, indices).det())
            if determinant.is_nonnegative is not True:
                raise AssertionError(f"{name}: principal minor {indices} = {determinant}")
    CHECKS.append(name + ': all principal minors')


def su2_chain_checks() -> None:
    imaginary = sp.I
    pauli = [sp.Matrix([[0, 1], [1, 0]]),
             sp.Matrix([[0, -imaginary], [imaginary, 0]]),
             sp.diag(1, -1)]
    generators = [-imaginary * matrix / 2 for matrix in pauli]
    identity = sp.eye(2)
    for alpha in range(3):
        for beta in range(3):
            equal(f'generator trace {alpha},{beta}',
                  sp.trace(generators[alpha] * generators[beta]),
                  -sp.Rational(int(alpha == beta), 2))
    links = [sp.Rational(3, 5)*identity-sp.I*sp.Rational(4, 5)*pauli[0],
             sp.Rational(5, 13)*identity-sp.I*sp.Rational(12, 13)*pauli[1],
             sp.Rational(8, 17)*identity-sp.I*sp.Rational(15, 17)*pauli[2],
             sp.Rational(7, 25)*identity-sp.I*sp.Rational(24, 25)*pauli[0]]
    for index, link in enumerate(links):
        equal(f'SU2 unitarity {index}', link.conjugate().T*link, identity)
        equal(f'SU2 determinant {index}', link.det(), 1)
    for b in range(1, 5):
        prefix = identity
        adjoints = []
        for j in range(b):
            adjoint = sp.Matrix(3, 3, lambda a, c:
                sp.expand(-2*sp.trace(generators[a]*prefix*generators[c]*prefix.conjugate().T)))
            equal(f'adjoint orthogonality {b},{j}', adjoint*adjoint.T, sp.eye(3))
            adjoints.append(adjoint)
            prefix = (prefix*links[j]).applyfunc(sp.expand)
        product = prefix
        initial_product = identity
        for link in links[:b-1]:
            initial_product = (initial_product*link).applyfunc(sp.expand)
        equal(f'chain inverse b={b}', initial_product.inv()*product, links[b-1])
        derivative = sp.Matrix.hstack(*adjoints)
        horizontal = derivative / b
        equal(f'pushforward horizontal b={b}', derivative*horizontal.T, sp.eye(3))
        equal(f'horizontal coefficient Gram b={b}',
              horizontal*horizontal.T, sp.eye(3)/b)
        projection = b*horizontal.T*horizontal
        equal(f'horizontal projection idempotence b={b}', projection**2, projection)
        equal(f'horizontal projection symmetry b={b}', projection.T, projection)
        vector = sp.Matrix(range(1, 3*b+1))
        equal(f'horizontal vertical energy decomposition b={b}',
              (vector.T*vector)[0],
              b*((horizontal*vector).T*(horizontal*vector))[0]
              +(((sp.eye(3*b)-projection)*vector).T*
                ((sp.eye(3*b)-projection)*vector))[0])
    reference, relative = links[0], links[1]
    target = reference*relative
    equal('smooth section relative factor', reference.inv()*target, relative)
    equal('smooth section ordered reconstruction', reference*relative, target)
    a, eps, i0, i1, j0, j1, jchi, k0, k1 = sp.symbols(
        'a eps I0 I1 J0 J1 Jchi K0_squared K1_squared', positive=True)
    factor = (1/a)**2*(1/(eps*a))**2*a*(eps*a)**2
    equal('tube curvature scaling retains physical a', factor, 1/a)
    equal('tube curvature complete profile factors',
          factor*jchi*(j0*k0/i0**2+j1*k1/i1**2),
          jchi/a*(j0*k0/i0**2+j1*k1/i1**2))
    h, z = sp.symbols('H z', nonzero=True)
    equal('S6 line inverse first composition', (z/h)*h, z)
    equal('S6 line inverse second composition', (z*h)/h, z)
    for epsilon in (-1, 1):
        for order in (3, 4):
            equal(f'S6 retained deck exponent {epsilon},{order}',
                  sp.Rational(epsilon*epsilon, order), sp.Rational(1, order))


def conditional_density_checks() -> None:
    # Exact smooth probability fixture on a two-torus, with Haar factors (2pi)^-1.
    w, z = sp.symbols('w z', real=True)
    coefficient = sp.Rational(1, 3)
    rho = 1+coefficient*sp.cos(w)*sp.cos(z)
    f = sp.sin(w)+sp.cos(z)
    def mean_z(expression):
        return sp.simplify(sp.integrate(sp.expand_trig(sp.expand(expression)),
                                       (z, -sp.pi, sp.pi))/(2*sp.pi))
    def mean_w(expression):
        return sp.simplify(sp.integrate(sp.expand_trig(sp.expand(expression)),
                                       (w, -sp.pi, sp.pi))/(2*sp.pi))
    marginal = mean_z(rho)
    equal('conditional marginal', marginal, 1)
    g = mean_z(f*rho)
    equal('conditional actual mean', g, sp.sin(w)+coefficient*sp.cos(w)/2)
    h = f-g
    equal('conditional fluctuation kernel', mean_z(h*rho), 0)
    score_times_rho = sp.diff(rho, w)
    equal('conditional score mean zero', mean_z(score_times_rho), 0)
    covariance = mean_z(h*score_times_rho)
    equal('conditional score covariance', covariance, -coefficient*sp.sin(w)/2)
    equal('conditional derivative identity', sp.diff(g, w),
          mean_z(sp.diff(f, w)*rho)+covariance)
    equal('fluctuation derivative identity', mean_z(sp.diff(h, w)*rho), -covariance)
    original_energy = mean_w(mean_z(rho*(sp.diff(f,w)**2+sp.diff(f,z)**2)))
    first_square = mean_w((sp.diff(g,w)-covariance)**2)
    second_square = mean_w(mean_z(rho*(sp.diff(h,w)+covariance)**2))
    vertical_square = mean_w(mean_z(rho*sp.diff(h,z)**2))
    equal('Dirichlet full square identity', original_energy,
          first_square+second_square+vertical_square)
    equal('Dirichlet fixture full energy', original_energy, 1)
    cross = -2*mean_w(sp.diff(g,w)*covariance)
    equal('Dirichlet retained cross energy', cross, -coefficient**2/4)
    equal('raw variance decomposition', mean_w(mean_z(rho*f**2)),
          mean_w(g**2)+mean_w(mean_z(rho*h**2)))


def schur_checks() -> None:
    s, lam = sp.symbols('s lambda', positive=True)
    # A positive block built from its exact complete-square factorization.
    d = sp.diag(2, 5)
    c = sp.Matrix([[1, 2], [3, -1]])
    remainder = sp.Matrix([[2, 1], [1, 2]])
    raw = sp.Matrix([[1, 1], [0, 2]])
    top = c.T*d.inv()*c+remainder
    a = top.row_join(c.T).col_join(c.row_join(d))
    r = raw.col_join(sp.zeros(2, 2))
    gram = r.T*r
    p = r*gram.inv()*r.T
    q = sp.eye(4)-p
    k = r.T*a*r
    b = q*a*r
    extended_d = q*a*q
    memory = sp.simplify(b.T*(extended_d+s*sp.eye(4)).inv()*b)
    expected = raw.T*c.T*(d+s*sp.eye(2)).inv()*c*raw
    equal('raw Schur memory', memory, expected)
    f = k+s*gram-memory
    lift = r-(extended_d+s*sp.eye(4)).inv()*b
    equal('raw projection idempotence', p*p, p)
    equal('restored boundary equation', q*(a+s*sp.eye(4))*lift, sp.zeros(4,2))
    equal('restored raw metric', f.diff(s), lift.T*lift)
    equal('restored energy identity', f, lift.T*(a+s*sp.eye(4))*lift)
    equal('two original Gram factors in resolvent',
          r.T*(a+s*sp.eye(4)).inv()*r, gram*f.inv()*gram)
    m0 = memory.subs(s, 0)
    equal('inverse energy budget remainder', k-m0, raw.T*remainder*raw)
    positive('inverse energy budget', k-m0)
    residues = []
    for j, energy in enumerate((sp.Integer(2), sp.Integer(5))):
        row = (c*raw)[j, :]
        residues.append((energy, row.T*row))
    equal('full memory residue representation', memory,
          sum((residue/(energy+s) for energy,residue in residues), sp.zeros(2)))
    equal('full inverse energy residue representation', m0,
          sum((residue/energy for energy,residue in residues), sp.zeros(2)))
    for eps in (sp.Rational(1,2), sp.Integer(2), sp.Integer(3), sp.Integer(5), sp.Integer(7)):
        low = sum((residue for energy,residue in residues if energy <= eps), sp.zeros(2))
        positive(f'linear infrared bound epsilon={eps}', eps*k-low)
    for parameter in (sp.Rational(1,3), sp.Integer(1), sp.Integer(4)):
        positive(f'memory at s={parameter}', memory.subs(s, parameter))
        positive(f'uniform memory budget at s={parameter}', k-memory.subs(s,parameter))
        positive(f'restored metric bound at s={parameter}',
                 (gram+k/(4*s)-f.diff(s)).subs(s,parameter))
        positive(f's Fprime <= F at s={parameter}',
                 (f-s*f.diff(s)).subs(s,parameter))
    for order in range(1,9):
        kernel = lam/(lam+s)**(order+1)
        equal(f'derivative maximum sign numerator r={order}',
              sp.diff(kernel,lam)*(lam+s)**(order+2), s-order*lam)
        maximum = sp.Rational(order**order, (order+1)**(order+1))/s**order
        equal(f'exact derivative bound constant r={order}', kernel.subs(lam,s/order), maximum)
    # Endpoint mass in the inverse measure, with all regulator factors retained.
    n = sp.symbols('n', positive=True, integer=True)
    alpha_total = sp.Rational(3,7)
    energy = 1/n
    sigma_mass = energy*alpha_total
    ms = sigma_mass/(energy+s)
    equal('inverse-memory finite zero value', ms.subs(s,0), alpha_total)
    equal('inverse-memory regulator limit at positive s', sp.limit(ms,n,sp.oo), 0)
    equal('inverse-memory endpoint budget', sp.limit(sigma_mass/energy,n,sp.oo), alpha_total)
    # Hermitian imaginary part for a complex off-diagonal residue.
    weight = sp.Matrix([[1, sp.I], [-sp.I, 1]])
    real, imaginary = sp.symbols('x eta', real=True)
    resolvent = weight/(2-real-sp.I*imaginary)
    im_matrix = (resolvent-resolvent.conjugate().T)/(2*sp.I)
    equal('matrix imaginary part preserves complex residue', im_matrix,
          imaginary*weight/((2-real)**2+imaginary**2))


def walsh_checks() -> None:
    for n in range(2,7):
        configurations = list(itertools.product((-1,1), repeat=n))
        subsets = [(), (1,), (n,), (1,n)]
        def character(subset, omega):
            result = 1
            for index in subset:
                result *= omega[index-1]
            return result
        for subset in subsets:
            rate = sp.Integer(len([j for j in subset if j != n]))
            rate += sp.Rational(int(n in subset),n)
            values = []
            for omega in configurations:
                value = 0
                for j in range(1,n+1):
                    flipped = list(omega)
                    flipped[j-1] *= -1
                    coefficient = sp.Rational(1,n) if j == n else sp.Integer(1)
                    value += coefficient*(character(subset,omega)-character(subset,flipped))/2
                values.append(value-rate*character(subset,omega))
            equal(f'Walsh generator n={n}, S={subset}', sp.Matrix(values), sp.zeros(2**n,1))
        low_values = [character((n,),omega) for omega in configurations]
        equal(f'escaping-label norm n={n}',
              sum(value**2 for value in low_values)/sp.Integer(2**n), 1)
        equal(f'escaping-label overlap fixed label 1 n={n}',
              sum(character((1,),omega)*character((n,),omega)
                  for omega in configurations)/sp.Integer(2**n), 0)
        equal(f'escaping-label energy n={n}',
              sum(sp.Rational(1,n)*value**2 for value in low_values)/sp.Integer(2**n),
              sp.Rational(1,n))
        fixed_rate = sum(sp.Rational(1,n) if j == n else sp.Integer(1) for j in (1,))
        equal(f'fixed-label energy n={n}', fixed_rate, 1)
    for n in range(2,6):
        coarse_norm = sum((2*w[0]+3*w[1])**2 for w in
                          itertools.product((-1,1), repeat=n))/sp.Integer(2**n)
        fine_norm = sum((2*w[0]+3*w[1])**2 for w in
                        itertools.product((-1,1), repeat=n+1))/sp.Integer(2**(n+1))
        equal(f'Walsh pullback raw norm n={n}', fine_norm, coarse_norm)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    su2_chain_checks()
    conditional_density_checks()
    schur_checks()
    walsh_checks()
    note = Path(__file__).with_name('RESEARCH_NOTE.md')
    result = {
        'status': 'passed', 'arithmetic': 'exact SymPy integer/rational/symbolic',
        'check_count': len(CHECKS), 'checks': CHECKS,
        'note_sha256': hashlib.sha256(note.read_bytes()).hexdigest(),
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope': 'Declared finite algebraic fixtures only; analytic proofs are in the note. No Yang--Mills vacuum or continuum mass has been numerically computed.'
    }
    text = json.dumps(result, indent=2, ensure_ascii=False)+'\n'
    if args.output:
        args.output.write_text(text, encoding='utf-8')
    print(text)


if __name__ == '__main__':
    main()
