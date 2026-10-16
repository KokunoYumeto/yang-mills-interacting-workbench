from fractions import Fraction as F
from pathlib import Path
import json
from weak_energy_constants import constants as weak
from evaluate_weighted_cubic import constants as weighted
from contracted_constants import Growth, minimum, mp

def constants(j,k='0.8',theta=1):
    old=weak(j,k,theta)
    jj=Growth(j,1,1);kap=Growth(k);a=1/(100*jj)
    b=1/(kap*a*a);z=Growth(theta)*kap/jj
    e1=F(21,4)*z;e2=F(21,4)*z*z;e3=z**3
    orig=old['old']['original'];Nq=orig['Nq'];Mq=orig['Mq'];Cq=orig['Cq']
    Gedge=minimum(8/(kap*kap*a*a),(2+2*mp.sqrt(4+2*mp.pi))/(kap*a))
    alpha=minimum(orig['AQ'],Nq**F(1,2)*Gedge)
    tr=old['trial'].copy()
    new20=old['EL']/kap+2*alpha*old['E1']
    tr[2,0]=minimum(tr[2,0],new20)
    # The original WCR estimates receive the improved proved D20 ceiling.
    new11=old['E32']/kap**F(3,2)+2*old['K']*old['E1']+2*orig['AQ']*tr[2,0]
    tr[1,1]=minimum(tr[1,1],new11)
    new02=old['M2']/kap**2+4*orig['AQ']*tr[1,1]+4*old['HH'][2,0]*tr[2,0]+2*old['VV'][1,0]*old['E1']/kap
    tr[0,2]=minimum(tr[0,2],new02)
    # PSE19 on each original Xi t, then on Delta_Q t.
    new30=old['E32']/kap**F(3,2)+(2*old['K']+Gedge)*old['E1']+2*alpha*tr[2,0]
    new21=tr[0,2]+4*alpha*tr[1,1]
    old30=((old['E32']/kap**F(3,2)+(2*old['K']+Gedge)*old['E1'])**2+2*old['K']*tr[2,0]**2)**F(1,2)
    old21=((tr[0,2]+2*alpha*tr[1,1])**2+2*old['K']*tr[1,1]**2)**F(1,2)
    d30=minimum(minimum(old['DD'][3,0],old30),new30)
    d21=minimum(minimum(old['DD'][2,1],old21),new21)
    p1=2*b*(4*Mq+Cq)**F(1,2);p2=3*b*(16*Mq+Cq)**F(1,2)
    px=2*b*Cq**F(1,2);p2x=3*b*Cq**F(1,2)
    pp=6*b*(4*Mq+Cq)**F(1,2);Ap=2*mp.pi*(2/(kap*a))*(Nq+3*Cq)**F(1,2)
    U=old['old']['Ul']
    def coeff(pf,p2f):
        return {(1,2):6*kap**3*U[1],(2,1):12*kap**3*U[2],(3,0):8*kap**3*U[3],
            (1,1):6*kap*kap*pf+4*e1*kap*kap*U[1],
            (2,0):8*kap*kap*p2f+12*kap*kap*p1*orig['AQ']+4*e1*kap*kap*U[2],
            (1,0):6*kap*kap*pf+4*kap*kap*pp*Ap+2*e1*kap*pf+2*e2*kap*U[1]}
    dc=coeff(p1,p2);rc=coeff(px,p2x)
    rest=(1+e1*kap*kap*tr[0,2]+e2*kap*tr[0,1]+e3*old['E0']+
          dc[2,1]*d21+dc[3,0]*d30+dc[1,1]*tr[1,1]+dc[2,0]*tr[2,0]+dc[1,0]*tr[1,0])/kap**3
    Y=4*alpha*tr[0,2]+(16*alpha**2*tr[0,2]**2+tr[0,2]*rest)**F(1,2)
    X=6*alpha*Y+rest
    d12=minimum(old['DD'][1,2],Y);d03=minimum(old['DD'][0,3],X)
    der={(1,2):d12,(2,1):d21,(3,0):d30,(1,1):tr[1,1],(2,0):tr[2,0],(1,0):tr[1,0]}
    rows={mr:rc[mr]*der[mr] for mr in rc}
    beta=sum(rows.values());direct=beta**2/z
    # Recompute every full WCR pair term with the new derivative ceilings.
    ft={mr:old['C'][mr]*tr[mr] for mr in old['C']}
    st={mr:(old['T'][mr]+2*old['old']['Ug'][1]*old['C'][mr])*tr[mr] for mr in old['C']}
    pair=sum(ft.values())**2/kap+sum(st.values())**2/z
    prior=weighted(j,k,theta)
    return dict(j=str(j),k=str(k),theta=str(theta),new20=new20,new11=new11,new02=new02,
        new30=new30,new21=new21,d30=d30,d21=d21,d12=d12,d03=d03,rest=rest,
        tr=tr,rows=rows,beta=beta,direct=direct,pair=pair,
        best=minimum(prior['best'],minimum(pair,direct)),prior=prior)

if __name__=='__main__':
    result=[]
    for j in [4,16,10**8,10**32]:
        x=constants(j)
        r=dict(j=x['j'],degrees={n:str(x[n].degree) for n in ['new20','new11','new02','new30','new21','d30','d21','d12','d03','rest','direct','pair']},
            row_degrees={str(k):str(v.degree) for k,v in x['rows'].items()},
            leading_direct_vs_WKM=str(x['direct'].leading/x['prior']['direct_energy'].leading),
            finite_direct_vs_WKM=str(x['direct'].value/x['prior']['direct_energy'].value),
            leading_pair_vs_WCR=str(x['pair'].leading/x['prior']['old']['energy'].leading))
        result.append(r);print(json.dumps(r))
    (Path(__file__).parent/'POSITIVE_RECEIVER_EVALUATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
