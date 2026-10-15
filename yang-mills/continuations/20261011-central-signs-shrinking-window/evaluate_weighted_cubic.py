from pathlib import Path
from fractions import Fraction as F
import json
from weak_energy_constants import constants as old_constants
from contracted_constants import Growth,minimum,mp,mpf
O=Path(__file__).resolve().parent
def constants(j,k='0.8',theta=1):
    old=old_constants(j,k,theta)
    jj=Growth(j,1,1)
    kap=Growth(k)
    z=Growth(theta)*kap/jj
    a=1/(100*jj)
    b=1/(kap*a*a)
    Nq=old['old']['original']['Nq']
    Cq=old['old']['original']['Cq']
    Gedge=minimum(8/(kap*kap*a*a),(2+2*mp.sqrt(4+2*mp.pi))/(kap*a))
    AQ=Nq*Gedge*Gedge
    Mx=2*b*Cq
    t02=old['trial'][0,2]
    ell=kap*(old['DD'][0,3]+2*AQ**F(1,2)*old['DD'][1,2])
    kinetic=((4*Mx*Mx*t02*t02+ell*ell)/(kap*kap))**F(1,2)
    score=mp.sqrt(3)*AQ*t02
    # Exact original energy identities for D^3 t and D^2 Delta t,
    # followed by the entire original cubic compression equation.
    aa=minimum(AQ**F(1,2),old['old']['original']['AQ'])
    t11=old['trial'][1,1]
    t20=old['trial'][2,0]
    b30=((old['E32']/kap**F(3,2)+(2*old['K']+Gedge)*old['E1'])**2+
         2*old['K']*t20*t20)**F(1,2)
    b21=((t02+2*aa*t11)**2+2*old['K']*t11*t11)**F(1,2)
    d30=minimum(old['DD'][3,0],b30)
    d21=minimum(old['DD'][2,1],b21)
    e1=F(21,4)*z
    e2=F(21,4)*z*z
    e3=z**3
    U=old['old']['Ul']
    Mq=old['old']['original']['Mq']
    AQold=old['old']['original']['AQ']
    cgeom=2/(kap*a)
    Ap=2*mp.pi*cgeom*(Nq+3*Cq)**F(1,2)
    p1=2*b*(4*Mq+Cq)**F(1,2)
    p2=3*b*(16*Mq+Cq)**F(1,2)
    px=2*b*Cq**F(1,2)
    p2x=3*b*Cq**F(1,2)
    p2p=6*b*(4*Mq+Cq)**F(1,2)
    def coefficients(pf,p2f):
        return {(1,2):6*kap**3*U[1],(2,1):12*kap**3*U[2],(3,0):8*kap**3*U[3],
                (1,1):6*kap*kap*pf+4*e1*kap*kap*U[1],
                (2,0):8*kap*kap*p2f+12*kap*kap*p1*AQold+4*e1*kap*kap*U[2],
                (1,0):6*kap*kap*pf+4*kap*kap*p2p*Ap+2*e1*kap*pf+2*e2*kap*U[1]}
    dc=coefficients(p1,p2)
    rc=coefficients(px,p2x)
    rest6=(1+e1*kap*kap*t02+e2*kap*old['trial'][0,1]+e3*old['E0']+
           dc[2,1]*d21+dc[3,0]*d30+dc[1,1]*t11+dc[2,0]*t20+dc[1,0]*old['trial'][1,0])/kap**3
    y=4*aa*t02+(16*aa*aa*t02*t02+t02*rest6)**F(1,2)
    x=6*aa*y+rest6
    d12=minimum(old['DD'][1,2],y)
    d03=minimum(old['DD'][0,3],x)
    ell_new=kap*(d03+2*aa*d12)
    derivative={(1,2):d12,(2,1):d21,(3,0):d30,(1,1):t11,(2,0):t20,(1,0):old['trial'][1,0]}
    direct_terms={mr:rc[mr]*derivative[mr] for mr in rc}
    beta=sum(direct_terms.values())
    direct_energy=beta*beta/z
    kinetic_new=((4*Mx*Mx*t02*t02+ell_new*ell_new)/(kap*kap))**F(1,2)
    snew2=6*kap**3*(kinetic_new+score)
    fnew=6*kap**3*AQ**F(1,2)*t02
    snew=6*kap**3*(kinetic+score)
    rest=[x for x in old['C'] if x!=(0,2)]
    fsum=fnew+sum(old['fterms'][x] for x in rest)
    ssum=snew+sum(old['sterms'][x] for x in rest)
    energy=fsum*fsum/kap+ssum*ssum/z
    ssum2=snew2+sum(old['sterms'][x] for x in rest)
    weighted_energy=fsum*fsum/kap+ssum2*ssum2/z
    best=minimum(minimum(weighted_energy,direct_energy),old['best'])
    df=old['fterms'][0,2].value-fnew.value
    ds=snew.value-old['sterms'][0,2].value
    den=df*df/mpf(k)+ds*ds/z.value
    lam=max(mp.mpf(0),min(mp.mpf(1),(old['Fsum'].value*df/mpf(k)-old['Ssum'].value*ds/z.value)/den)) if den else mp.mpf(0)
    mixed=(old['Fsum'].value-lam*df)**2/mpf(k)+(old['Ssum'].value+lam*ds)**2/z.value
    return dict(j=str(j),k=str(k),theta=str(theta),old=old,AQ=AQ,Mx=Mx,ell=ell,
        kinetic=kinetic,score=score,fnew=fnew,snew=snew,Fsum=fsum,Ssum=ssum,
        energy=energy,best=best,lambda_upper=lam,interpolated_energy=mixed,
        b30=b30,b21=b21,d30=d30,d21=d21,rest6=rest6,d12=d12,d03=d03,ell_new=ell_new,
        beta=beta,direct_energy=direct_energy,direct_terms=direct_terms,
        weighted_energy=weighted_energy,kinetic_new=kinetic_new,snew2=snew2)
def report(d):
    names=['AQ','Mx','ell','kinetic','score','fnew','snew','Fsum','Ssum','energy','best',
           'b30','b21','d30','d21','rest6','d12','d03','ell_new','beta','direct_energy','weighted_energy']
    return dict(j=d['j'],k=d['k'],theta=d['theta'],
        degrees={n:str(d[n].degree) for n in names},
        values={n:mp.nstr(d[n].value,35) for n in names},
        log10_energy=mp.nstr(mp.log10(d['energy'].value),35),
        log10_old_energy=mp.nstr(mp.log10(d['old']['energy'].value),35),
        ratio_new_old=mp.nstr(d['energy'].value/d['old']['energy'].value,35),
        ratio_direct_old=mp.nstr(d['direct_energy'].value/d['old']['energy'].value,35),
        ratio_weighted_old=mp.nstr(d['weighted_energy'].value/d['old']['energy'].value,35),
        leading_ratio_direct_old=mp.nstr(d['direct_energy'].leading/d['old']['energy'].leading,35),
        leading_ratio_weighted_old=mp.nstr(d['weighted_energy'].leading/d['old']['energy'].leading,35),
        lambda_upper=mp.nstr(d['lambda_upper'],35),
        old_row_degrees={str(mr):dict(flux=str(d['old']['fterms'][mr].degree),scalar=str(d['old']['sterms'][mr].degree)) for mr in d['old']['C']},
        derivative_degrees={str(mr):str(d['old']['DD'][mr].degree) for mr in [(0,3),(1,2)]})
if __name__=='__main__':
    rows=[report(constants(j)) for j in [4,16,10**8,10**32]]
    (O/'WEIGHTED_CUBIC_EVALUATION.json').write_text(json.dumps(dict(scope='Complete positive finite upper functions, not sampled Wilson-state moments.',rows=rows),indent=2)+'\n',encoding='utf8',newline='\n')
    for row in rows:
        print(json.dumps({k:v for k,v in row.items() if k!='values'}))
