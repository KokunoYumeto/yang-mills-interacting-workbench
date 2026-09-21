"""Exact fourth-source total-/point-spin bounds in the original coefficients."""
from source_engine import *
from exact_lp import maximize

def compute_budgets(pcoeff,pbound,transports):
    sm=F(0);st=F(0);data=[]
    for row,br,tr in zip(pcoeff,pbound['rows'],transports):
     ps=tuple(tuple(p) for p in row['faces']);o=Source(ps);ws,edges=o.words,o.edges;cs=tuple(ps.count(p) for p in o.ps);f=o.v(cs);sp,allowed=physical_spectrum(tuple(w for w,k in zip(ws,cs) for _ in range(k)),edges)
     es=sorted(edges);byj=[dict(zip(es,map(lambda x:F(x,2),jj))) for jj in allowed];byj=[j for j in byj if sum(j.values())]
     bd=F(br['selected_bound']);rbm=bd*max(sum(j.values())/sum(x*(x+1) for x in j.values()) for j in byj)
     rbt={e:bd*max(j[e]/sum(x*(x+1) for x in j.values()) for j in byj) for e in es}
     tm=F(0);tt={e:F(0) for e in es}
     for mm,c in f.items():
      tbd=abs(c)*2**sum(len(w)-1 for w in mm);occ=Counter(abs(x) for w in mm for x in w)
      tm+=tbd*F(sum(occ.values()),2)
      for e in es:tt[e]+=tbd*F(occ[e],2)
     bm=min(rbm,tm);bt={e:min(rbt[e],tt[e]) for e in es};cert=[]
     spin=br['spin_certificate']
     if spin:
      she=spin['shared_edges'];cnt=Counter(abs(x) for w in ws for x in w);channels=[]
      for bits,c,a in spin['channels']:
       js={e:F(bits[she.index(e)]) if cnt[e]==2 else F(1,2) for e in es};channels.append((js,F(a)))
      A=[[int(all(j[e]==0 for i,e in enumerate(she) if mask>>i&1)) for j,a in channels] for mask in range(1<<len(she))]
      bs=list(map(F,spin['partial_projection_bounds']))
      seen={}
      for name,sel in [('total',lambda j:sum(j.values()))]+[(str(e),lambda j,e=e:j[e]) for e in es]:
       weights=tuple(abs(a)*sel(j) for j,a in channels)
       if weights not in seen:seen[weights]=maximize(A,bs,weights)
       v,x,y,k=seen[weights];cert.append({'name':name,'bound':str(v),'dual':list(map(str,y))})
       if name=='total':bm=min(bm,v)
       else:bt[int(name)]=min(bt[int(name)],v)
     hist=Counter()
     for image in tr['images']:
      pm=image['permutation'];ss=image['signs'];off=image['offset']
      uu=tuple(-off[i] for i in range(3));vv=tuple(ss[i]*int(pm[i]==0)-off[i] for i in range(3))
      e=next(e for e,ed in edges.items() if set(ed)=={uu,vv});hist[e]+=1
     sm+=len(tr['images'])*bm;st+=sum(n*bt[e] for e,n in hist.items())
     data.append({'index':row['index'],'m':str(bm),'t':{str(e):str(v) for e,v in bt.items()},'anchor_multiplicity':dict(hist),'duals':cert})
    return {'M4':str(sm),'T4':str(st),'rows':data}
