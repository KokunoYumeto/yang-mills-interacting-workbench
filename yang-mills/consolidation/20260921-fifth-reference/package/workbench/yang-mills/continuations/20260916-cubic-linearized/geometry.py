from itertools import combinations
from collections import defaultdict, Counter

def add(n,i,k=1):
    v=list(n);v[i]+=k;return tuple(v)
def edge(n,i):return tuple(n)+(i,)
def endpoints(e):return e[:3],add(e[:3],e[3])
def pword(p):
    n,i,j=p[:3],p[3],p[4]
    return ((edge(n,i),1),(edge(add(n,i),j),1),(edge(add(n,j),i),-1),(edge(n,j),-1))
def pedges(p):return frozenset(e for e,s in pword(p))
def incident(e):
    n,i=e[:3],e[3];out=[]
    for j in range(3):
        if j==i:continue
        a,b=sorted((i,j))
        out += [tuple(n)+(a,b),add(n,j,-1)+(a,b)]
    return tuple(sorted(out))
def adjacent(p):
    return frozenset(q for e in pedges(p) for q in incident(e) if q!=p)
def union(ps):return frozenset().union(*(pedges(p) for p in ps))
def boundary(ps):
    c=Counter(e for p in ps for e in pedges(p));return frozenset(e for e,n in c.items() if n%2)
def cycle(es):
    adj=defaultdict(list)
    for e in es:
        u,v=endpoints(e);adj[u].append((v,e,1));adj[v].append((u,e,-1))
    if any(len(x)!=2 for x in adj.values()):raise ValueError('boundary is not a cycle')
    root=min(adj);at=root;last=None;out=[]
    while True:
        opts=sorted(x for x in adj[at] if x[1]!=last)
        v,e,s=opts[0];out.append((e,s));last=e;at=v
        if at==root:break
        if len(out)>len(es):raise ValueError('unclosed')
    if len(out)!=len(es):raise ValueError('disconnected boundary')
    return tuple(out)
def type3(ps):
    if len(set(ps))==1:return 'self'
    if len(set(ps))==2:return 'repeat' if any(len(pedges(p)&pedges(q)) for p,q in combinations(set(ps),2)) else 'disconnected'
    links=[pedges(p)&pedges(q) for p,q in combinations(ps,2)]
    count=sum(bool(x) for x in links)
    if count<2:return 'disconnected'
    if count==2:return 'path'
    if set.intersection(*(set(pedges(p)) for p in ps)):return 'common'
    return 'corner'
def anchored():
    anchor=(0,0,0,0)
    tris=set();pairs=set()
    for p in incident(anchor):
        for q in adjacent(p):
            pairs.add(tuple(sorted((p,q))))
            for r in adjacent(p)|adjacent(q):
                if r not in (p,q):tris.add(tuple(sorted((p,q,r))))
    out={t:[] for t in ('path','common','corner')}
    for ps in sorted(tris):out[type3(ps)].append(ps)
    return anchor, sorted(pairs),out
if __name__=='__main__':
    a,ps,ts=anchored();print('pairs',len(ps));print({k:len(v) for k,v in ts.items()})
    for k,xs in ts.items():
        print(k,'example',xs[0], 'union',len(union(xs[0])))
        if k in ('path','corner'):
            print('boundary histogram',Counter(len(cycle(boundary(x))) for x in xs))
    print('pair boundaries',Counter(len(cycle(boundary(x))) for x in ps))
