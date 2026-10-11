from pathlib import Path
import math,json
import numpy as np

root=Path(__file__).resolve().parent

def qmul(a,b):
    return np.r_[a[0]*b[0]-np.dot(a[1:],b[1:]),a[0]*b[1:]+b[0]*a[1:]+np.cross(a[1:],b[1:])]

def qexp(t,axis):
    return np.r_[math.cos(t/2),math.sin(t/2)*np.asarray(axis)]

def qinv(a):
    return a*np.array([1,-1,-1,-1])

def direct_word_checks():
    tests=[]
    e1=np.array([1.,0.,0.]);e3=np.array([0.,0.,1.])
    for n in [3,5,9,17]:
        m=n-1
        v=np.sqrt(2/n)*np.cos(math.pi*(np.arange(n)+.5)/n)
        w=-np.sqrt(2/n)*np.sin(math.pi*(np.arange(m)+1)/n)
        for k,l in [(0,0),(m//2-1,m//2),(m-1,m-1)]:
            a=w[k]*v[l]/math.sqrt(2*n);b=-v[k+1]*w[l]/math.sqrt(2*n)
            c=w[k]*v[l+1]/math.sqrt(2*n);d=-v[k]*w[l]/math.sqrt(2*n)
            delta=math.pi/m;phi=math.pi*(k+1)/m
            Uright=qexp(phi,e3);Uleft=qexp(math.pi*k/m,e3)
            for z in [e1,e3]:
                def original_defect(t):
                    edges=[qexp(t*a,z),qmul(qexp(t*b,z),Uright),qinv(qexp(t*c,z)),qinv(qmul(qexp(t*d,z),Uleft))]
                    product=np.array([1.,0.,0.,0.])
                    for edge in edges: product=qmul(product,edge)
                    return 2-2*product[0]
                if z[0]:
                    Js=[b*e1,-c*np.array([math.cos(phi),math.sin(phi),0]),(a-d)*np.array([math.cos(delta),math.sin(delta),0])]
                    J=sum(Js);Q=sum((np.cross(Js[i],Js[r]) for i in range(3) for r in range(i+1,3)),start=np.zeros(3))
                    exact=.5*math.cos(delta/2)*np.dot(J,J)+math.sin(delta/2)*Q[2]
                else: exact=.5*math.cos(delta/2)*(a+b-c-d)**2
                eps=.004
                second=(original_defect(eps)-2*original_defect(0)+original_defect(-eps))/eps**2
                error=abs(second-exact)
                assert error<8e-8,(n,k,l,z,error)
                tests.append({'n':n,'k':k,'l':l,'colour':int(1 if z[0] else 3),'direct_second':second,'exact_second':exact,'absolute_error':error})
    return tests

def general_word_checks():
    rng=np.random.default_rng(6112026);tests=[]
    def adjoint(q,z):
        c=q[0];v=q[1:]
        return (c*c-np.dot(v,v))*z+2*v*np.dot(v,z)+2*c*np.cross(v,z)
    for case in range(36):
        n=[3,5,9][case//12];m=n-1;k=case%m;l=(3*case+1)%m
        v=np.sqrt(2/n)*np.cos(math.pi*(np.arange(n)+.5)/n)
        w=-np.sqrt(2/n)*np.sin(math.pi*(np.arange(m)+1)/n)
        a=w[k]*v[l]/math.sqrt(2*n);b=-v[k+1]*w[l]/math.sqrt(2*n)
        c=w[k]*v[l+1]/math.sqrt(2*n);d=-v[k]*w[l]/math.sqrt(2*n)
        links=rng.normal(size=(4,4));links/=np.linalg.norm(links,axis=1)[:,None]
        z=rng.normal(size=3);z/=np.linalg.norm(z)
        A,B=links[0],links[1];C=qinv(links[2]);D=qinv(links[3])
        ABC=qmul(qmul(A,B),C);P=qmul(ABC,D)
        Js=[b*adjoint(A,z),-c*adjoint(ABC,z),(a-d)*adjoint(P,z)]
        J=sum(Js);Q=sum((np.cross(Js[i],Js[r]) for i in range(3) for r in range(i+1,3)),start=np.zeros(3))
        first=np.dot(P[1:],J);second=.5*P[0]*np.dot(J,J)+np.dot(P[1:],Q)
        def original(t):
            varied=[qmul(qexp(t*a,z),links[0]),qmul(qexp(t*b,z),links[1]),qinv(qmul(qexp(t*c,z),links[2])),qinv(qmul(qexp(t*d,z),links[3]))]
            product=np.array([1.,0.,0.,0.])
            for edge in varied:product=qmul(product,edge)
            return 2-2*product[0]
        eps=.002
        finitefirst=(original(eps)-original(-eps))/(2*eps)
        finitesecond=(original(eps)-2*original(0)+original(-eps))/eps**2
        assert abs(finitefirst-first)<1e-8
        assert abs(finitesecond-second)<2e-8
        tests.append({'case':case,'n':n,'first_error':abs(finitefirst-first),'second_error':abs(finitesecond-second)})
    return tests

def values(n,theta=math.pi):
    m=n-1;h=math.pi/(2*n);s=math.sin(h);c=math.cos(h)
    v=np.sqrt(2/n)*np.cos(math.pi*(np.arange(n)+.5)/n)
    w=-np.sqrt(2/n)*np.sin(math.pi*(np.arange(m)+1)/n)
    aa=w[:,None]*v[:-1][None,:]/math.sqrt(2*n)
    bb=-v[1:,None]*w[None,:]/math.sqrt(2*n)
    cc=w[:,None]*v[1:][None,:]/math.sqrt(2*n)
    dd=-v[:-1,None]*w[None,:]/math.sqrt(2*n)
    t1=bb;t2=-cc;t3=aa-dd
    lp=abs(t1)+abs(t2)+abs(t3)
    full=abs(aa)+abs(bb)+abs(cc)+abs(dd)
    B=n*np.sum(lp*lp)/2
    Bfull=n*np.sum(full*full)/2
    Bfull_exact=2*c*c*(1-2/n+(1/math.tan(h))**2/n**2)
    assert abs(Bfull-Bfull_exact)<2e-13
    assert np.max(full*full)<=8*c*c/n**3+1e-15
    assert abs(np.max(lp*lp)-8*c**4/n**3)<1e-14
    witness=(0,(n-3)//2)
    assert abs(lp[witness]**2-8*c**4/n**3)<1e-14
    sigma2=n*np.sum((aa+bb-cc-dd)**2)
    assert abs(sigma2-8*s*s)<1e-13
    delta=theta/m
    phi=theta*(np.arange(m)+1)/m
    rotphi=np.stack([np.cos(phi),np.sin(phi)],axis=1)[:,None,:]
    rotdelta=np.array([math.cos(delta),math.sin(delta)])
    J1=np.stack([t1,np.zeros_like(t1)],axis=2)
    J2=t2[:,:,None]*rotphi
    J3=t3[:,:,None]*rotdelta
    J=J1+J2+J3
    cross=lambda a,b:a[:,:,0]*b[:,:,1]-a[:,:,1]*b[:,:,0]
    Jp=cross(J1,J2)+cross(J1,J3)+cross(J2,J3)
    hess=n*np.sum(.5*math.cos(delta/2)*(J*J).sum(2)+math.sin(delta/2)*Jp)
    curl=n*np.sum(J*J)
    parallel=.5*sigma2*math.cos(delta/2)
    defect=2-2*math.cos(delta/2)
    error=abs(hess-.5*curl)
    eta=2*B*defect
    error_bound=eta/4+.5*math.sqrt(2*B*eta)
    assert error<=error_bound+1e-13
    # The complete row-weighted root depth, using every i coordinate and both edge directions.
    mean_i=m/2
    depth=.5*sum(w[k]**2*v[l]**2*(mean_i+k+l) for k in range(m) for l in range(n))
    depth+=.5*sum(v[k]**2*w[l]**2*(mean_i+k+l) for k in range(n) for l in range(m))
    assert abs(depth-(3*m-1)/2)<1e-12*n
    return {'n':n,'B_n':B,'B_full23':Bfull,'max_weight':float(np.max(lp*lp)),'sigma_squared':sigma2,'single_face_defect':defect,'transverse_hessian':hess,'parallel_hessian':parallel,'covariant_curl':curl,'error':error,'error_bound':error_bound,'weighted_depth':depth}

if __name__=='__main__':
    records=[values(n) for n in [3,5,9,17,33,65,129,257,513]]
    word_checks=direct_word_checks()
    general_checks=general_word_checks()
    limit=1.5+8/math.pi**2
    assert abs(records[-1]['B_n']-limit)<.02
    assert abs(records[-1]['transverse_hessian']-.5)<.02
    assert abs(records[-1]['covariant_curl']-1)<.04
    report={'records':records,'direct_original_word_checks':word_checks,'general_original_word_checks':general_checks,'B_limit':limit,'transverse_hessian_limit':.5,'covariant_curl_limit':1,'status':'all checks passed'}
    (root/'DIRECTIONAL_CHECKS.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({'status':report['status'],'last_box':records[-1],'B_limit':limit,'direct_word_checks':len(word_checks),'maximum_word_error':max(r['absolute_error'] for r in word_checks),'general_word_checks':len(general_checks),'maximum_general_second_error':max(r['second_error'] for r in general_checks)}))
