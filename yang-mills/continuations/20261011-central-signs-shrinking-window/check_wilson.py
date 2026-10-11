from pathlib import Path
from collections import Counter
import math,json
import numpy as np
from scipy.integrate import quad

root=Path(__file__).resolve().parent
def inv(w):return [(e,-s) for e,s in w[::-1]]
def path(i,k,l):
    return [((3,0,0,r),1) for r in range(l)]+[((2,0,r,l),1) for r in range(k)]+[((1,r,k,l),1) for r in range(i)]
def edge(d,i,k,l):return (d,i,k,l)
def chord(d,i,k,l):
    end=[i,k,l];end[d-1]+=1
    return path(i,k,l)+[(edge(d,i,k,l),1)]+inv(path(*end))
def reduce_word(w,cyclic=False):
    out=[]
    for letter in w:
        if out and out[-1]==(letter[0],-letter[1]):out.pop()
        else:out.append(letter)
    if cyclic:
        while len(out)>1 and out[0]==(out[-1][0],-out[-1][1]):
            out=out[1:-1]
    return out
def face(d,e,i,k,l):
    p=[i,k,l];pd=p.copy();pd[d-1]+=1;pe=p.copy();pe[e-1]+=1
    return [(edge(d,*p),1),(edge(e,*pd),1),(edge(d,*pe),-1),(edge(e,*p),-1)]
def rooted_face(d,e,i,k,l):return path(i,k,l)+face(d,e,i,k,l)+inv(path(i,k,l))
def root_surfaces(i,k,l):
    z2=sum((rooted_face(1,2,r,k,l) for r in reversed(range(i))),[])
    z3=sum((rooted_face(1,3,r,k,l) for r in reversed(range(i))),[])+sum((rooted_face(2,3,0,r,l) for r in reversed(range(k))),[])
    return z2,z3
def words(i,k,l):
    A=chord(2,i,k,l);B=chord(3,i,k+1,l);C=inv(chord(2,i,k,l+1));D=inv(chord(3,i,k,l))
    return [inv(A)+A+B+C,inv(A)+A+B+C+D,inv(A+B+C)+A+B+C+D],[B+C,B+C+D,D],[A,B,C,D]
def cross(z):
    x,y,z=z
    return np.array([[0,-z,y],[z,0,-x],[-y,x,0.]])
J=[cross(z) for z in np.eye(3)]
def qmul(a,b):
    return np.r_[a[0]*b[0]-np.dot(a[1:],b[1:]),a[0]*b[1:]+b[0]*a[1:]+np.cross(a[1:],b[1:])]
def qinv(a):return a*np.array([1,-1,-1,-1])
def fibre_checks():
    rng=np.random.default_rng(61128);rows=[]
    for case in range(12):
        qs=rng.normal(size=(3,4));qs/=np.linalg.norm(qs,axis=1)[:,None]
        B,C,D=qs;z=rng.normal(size=3);z/=np.linalg.norm(z)
        t=.371;exp=np.r_[math.cos(t/2),math.sin(t/2)*z]
        Bt=qmul(B,exp);Dt=qmul(qmul(qmul(qinv(C),qinv(exp)),C),D)
        original=qmul(qmul(B,C),D);moved=qmul(qmul(Bt,C),Dt)
        error=float(np.linalg.norm(original-moved))
        assert error<3e-15
        rows.append({'case':case,'fixed_product_error':error,'original_product_metric_speed_squared':2.0})
    return rows
def rotation(q):
    c=q[0];v=q[1:]
    return (c*c-np.dot(v,v))*np.eye(3)+2*np.outer(v,v)+2*c*cross(v)
def product_jets(word,rotations,target,colour):
    v=np.eye(3);d=np.zeros((3,3));dd=np.zeros((3,3))
    for e,s in word:
        R=rotations[e] if s==1 else rotations[e].T
        if e==target:
            Dr=J[colour]@R if s==1 else -R@J[colour]
            DDr=J[colour]@J[colour]@R if s==1 else R@J[colour]@J[colour]
        else:Dr=np.zeros((3,3));DDr=Dr
        v,d,dd=v@R,d@R+v@Dr,dd@R+2*d@Dr+v@DDr
    return float(np.trace(v)),float(np.trace(d)),float(np.trace(dd))
def word_checks():
    rng=np.random.default_rng(2026101128)
    records=[];jet_records=[]
    for n in [3,5,7]:
        m=n-1
        for i in range(n):
            for k in range(m):
                for l in range(m):
                    full,short,ABCD=words(i,k,l)
                    lengths=[2*i+2*k+4,2*i+4,0 if i==k==0 else 2*i+2*k+2]
                    z2,z3=root_surfaces(i,k,l)
                    assert reduce_word(z2)==reduce_word(chord(2,i,k,l))
                    assert reduce_word(z3)==reduce_word(chord(3,i,k,l))
                    surfaces=[inv(z2)+rooted_face(2,3,i,k,l)+z3,inv(z2)+rooted_face(2,3,i,k,l),inv(z3)]
                    for j,(w,s,area,ell) in enumerate(zip(full,short,surfaces,lengths)):
                        rw=reduce_word(w,True)
                        assert rw==reduce_word(s,True)
                        assert reduce_word(s)==reduce_word(area)
                        assert len(rw)==ell
                        assert len({e for e,sign in rw})==ell
                        counts=Counter(e for e,sign in w)
                        assert all(counts[e]>=1 for e,sign in rw)
                        records.append({'n':n,'i':i,'k':k,'l':l,'word':['BC','BCD','D'][j],'full_occurrences':len(w),'reduced_loop_length':ell,'mixed_Casimir_coefficient':2*(len(w)-ell)})
                    if (i,k,l) not in [(0,0,0),(0,m-1,m-1),(m,0,m//2),(m,m-1,m-1)]:continue
                    all_edges={e for w in full for e,sign in w}
                    rotations={}
                    for e in sorted(all_edges):
                        q=rng.normal(size=4);q/=np.linalg.norm(q);rotations[e]=rotation(q)
                    for j,(w,ell) in enumerate(zip(full,lengths)):
                        remaining={e for e,sign in reduce_word(w,True)}
                        counts=Counter(e for e,sign in w);total=0;gamma=0;max_cross_error=0
                        value=None
                        for e,count in counts.items():
                            jets=[product_jets(w,rotations,e,a) for a in range(3)]
                            value=jets[0][0]
                            lap=sum(r[2] for r in jets);grad=sum(r[1]**2 for r in jets)
                            total+=lap;gamma+=grad
                            cross_value=lap+2*count*value
                            max_cross_error=max(max_cross_error,abs(cross_value-2*(count-int(e in remaining))*value))
                        if value is None:value=3.
                        H=3-value
                        assert abs(total+2*ell*value)<2e-10
                        assert abs(gamma-ell*H*(4-H))<2e-10
                        assert max_cross_error<2e-10
                        jet_records.append({'n':n,'i':i,'k':k,'l':l,'word':['BC','BCD','D'][j],'chi':value,'loop_length':ell,'laplacian_error':abs(total+2*ell*value),'gradient_error':abs(gamma-ell*H*(4-H)),'maximum_mixed_term_error':max_cross_error})
    return records,jet_records

def coefficients(n,xi):
    m=n-1;h=math.pi/(2*n);s=math.sin(h);c=math.cos(h)
    v=np.sqrt(2/n)*np.cos(math.pi*(np.arange(n)+.5)/n)
    w=-np.sqrt(2/n)*np.sin(math.pi*(np.arange(m)+1)/n)
    tau=2*math.sqrt(xi);r=math.sqrt(tau/(1+tau))
    Q=0.;Pplus=0.;Pminus=0.;Bsum=0.;sigma2=0.;diag=0.;exception=0.;exception_abs=0.;varupper=0.
    for k in range(m):
        a=w[k]*v[:-1]/math.sqrt(2*n);b=-v[k+1]*w/math.sqrt(2*n)
        cv=w[k]*v[1:]/math.sqrt(2*n);d=-v[k]*w/math.sqrt(2*n)
        t1=b;t2=-cv;t3=a-d
        lower=np.maximum.reduce([t1*t1/(1+tau),t3*t3/(1+tau),t2*t2/(1+2*tau)])
        Q+=n*float(np.sum(lower))
        pairs=[t1*t2,t1*t3,t2*t3]
        Pplus+=n*sum(float(np.sum(np.maximum(t,0))) for t in pairs)
        Pminus+=n*sum(float(np.sum(np.maximum(-t,0))) for t in pairs)
        if k==0:
            tree=t1*t1+(t2+t3)**2-2*r*abs(t1*(t2+t3))
            Q+=float(np.sum(tree-lower))
            Pplus-=float(np.sum(np.maximum(pairs[2],0)))
            Pminus-=float(np.sum(np.maximum(-pairs[2],0)))
            exception=float(np.sum(pairs[2]))
            exception_abs=float(np.sum(abs(pairs[2])))
        diag+=n*float(np.sum(t1*t1+t2*t2+t3*t3))
        Bsum+=n*float(np.sum((abs(t1)+abs(t2)+abs(t3))**2))/2
        sigma2+=n*float(np.sum((t1+t2+t3)**2))
    explicit_exception=-s*s*v[0]**2/n*(2*math.cos(2*h)-2*v[0]**2-1)
    explicit_diag=2*(1-v[0]**2)+s*s
    assert abs(exception-explicit_exception)<2e-13
    assert abs(diag-explicit_diag)<2e-12
    A0=diag+2*exception
    assert abs(A0+2*(Pplus-Pminus)-sigma2)<4e-12
    assert abs(diag/2+Pplus+Pminus+exception_abs-Bsum)<4e-12
    q=math.sqrt(xi)
    gamma_plus=(3*q+3*math.sqrt(q*(1+4*q)))/(1+3*q)
    gamma_minus=(3*q-3*math.sqrt(q*(1+4*q)))/(1+3*q)
    upper=A0+(2/3)*(gamma_plus*Pplus-gamma_minus*Pminus)
    variable_upper=A0+2*r*(Pplus+Pminus)
    return {'n':n,'xi':xi,'r':r,'gamma_plus':gamma_plus,'gamma_minus':gamma_minus,'Q_lower':Q,'C_upper':min(2*Bsum,upper),'character_upper':upper,'variable_upper':variable_upper,'A0':A0,'P_plus':Pplus,'P_minus':Pminus,'sigma_squared':sigma2,'B_n':Bsum,'tree_cross_sum':exception,'tree_absolute_cross_sum':exception_abs}

def coefficient_integral():
    a=math.sqrt(2);b=2+a
    def inner(y):
        x1=math.atan(a*math.tan(y));x2=math.atan(b*math.tan(y))
        one=math.sin(y)**2*(x1/2+math.sin(2*x1)/4)
        two=.5*math.cos(y)**2*((x2-x1)/2-(math.sin(2*x2)-math.sin(2*x1))/4)
        three=(math.pi/2-x2)/2-(math.sin(2*y)-math.sin(2*x2-2*y))/4
        return one+two+three
    J,error=quad(inner,0,math.pi/2,epsabs=2e-13,epsrel=2e-13)
    value=2/math.pi**2*(math.pi**2/4+1+2*J)
    # Exact mathematical midpoint error is <= pi/N, from the unit L1 Lipschitz bound.
    # Floating evaluation is a numerical check, not an interval arithmetic certificate.
    N=2048;y=(np.arange(N)+.5)*math.pi/N;sy=np.sin(y);cy=np.cos(y);total=0.
    for x in (np.arange(N)+.5)*math.pi/N:
        p=math.sin(x)*cy;q=math.cos(x)*sy
        total+=float(np.sum(np.maximum.reduce([q*q,(p+q)**2,.5*p*p])))
    midpoint=2*total/N**2
    assert abs(value-midpoint)<math.pi/N
    assert 1<=value<=1.75
    return {'I':value,'opposite_quadrant_integral_J':J,'quadrature_error_report':error,'midpoint_N':N,'midpoint_value':midpoint,'exact_mathematical_midpoint_error_bound':math.pi/N,'numerical_values_are_not_interval_certificates':True}

if __name__=='__main__':
    records,jets=word_checks()
    fibres=fibre_checks()
    I=coefficient_integral()
    path_values=[]
    for j in range(1,7):
        row=coefficients(2*j**4+1,10000*j*j)
        row['j']=j;row['j_Q_lower']=j*row['Q_lower'];row['signed_lower']=row['Q_lower']-row['sigma_squared']
        row['Q_over_ordinary_curl']=row['Q_lower']/row['sigma_squared']
        path_values.append(row)
    out={'status':'all checks passed','word_occurrence_checks':records,'full_word_Casimir_checks':jets,'exact_two_link_fibre_checks':fibres,'integral':I,'original_path_kappa_star_1':path_values,'I_lower_analytic':1,'I_upper_analytic':1.75,'C_upper_limit':2+32/(3*math.pi**2)}
    (root/'WILSON_COVARIANCE_CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({'status':out['status'],'word_checks':len(records),'full_jet_checks':len(jets),'max_laplacian_error':max(t['laplacian_error'] for t in jets),'max_mixed_error':max(t['maximum_mixed_term_error'] for t in jets),'I':I,'path':path_values},indent=2))
