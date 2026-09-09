"""Exact arithmetic checks for fixed_coupling_analytic_disk_obstruction.md.

The checks verify only the finite-box counting and displayed inequalities;
they are not a continuum or mass-gap computation.
"""

from fractions import Fraction


def check() -> None:
    # M_L = 3 (2L)^2 (2L+1) = 12 L^2 (2L+1).
    for L in range(2, 31):
        m = 2 * L
        M_from_edges = 3 * m * m * (m + 1)
        M_closed = 12 * L * L * (2 * L + 1)
        assert M_from_edges == M_closed

        # 3/(16 M_L) = 1/(64 L^2 (2L+1)).
        disk = Fraction(3, 16 * M_closed)
        closed = Fraction(1, 64 * L * L * (2 * L + 1))
        assert disk == closed

        # ||xi W|| = 2 xi M and xi=1/(4g^4), with g=1 as an exact test.
        xi = Fraction(1, 4)
        interaction_norm = 2 * xi * M_closed
        assert interaction_norm == Fraction(M_closed, 2)

        # Ratio to the H_0 gap 3/4 is 8 M / 3 for g=1.
        ratio = interaction_norm / Fraction(3, 4)
        assert ratio == Fraction(2 * M_closed, 3)

    # For any fixed finite g, the disk condition fails eventually.  Exhibit
    # the exact threshold failure for several finite couplings.
    for g in (1, 2, 10, 100):
        g4 = g**4
        found_failure = False
        for j in range(1, 10000):
            disk_rhs = Fraction(1, 64 * j**4 * (2 * j**2 + 1))
            xi = Fraction(1, 4 * g4)
            if xi >= disk_rhs:
                found_failure = True
                break
        assert found_failure


if __name__ == "__main__":
    check()
    print("PASS: fixed-coupling analytic-disk obstruction checks")

