"""Exact original-link kinetic operator on a tree slice for small face clusters.

No regulator spectrum is spin-truncated. This computes finite perturbative
polynomials whose degree is justified order by order.
"""
from fractions import Fraction as Q
from itertools import product, combinations, combinations_with_replacement
from collections import defaultdict
from functools import lru_cache

def plus(n,i,delta=1):
    a=list(n); a[i]+=delta; return tuple(a)
def face_edges(p):
    n=p[:3];i,j=p[3:]
    return frozenset((n+(i,),plus(n,i)+(j,),plus(n,j)+(i,),n+(j,)))
def endpoints(e):return e[:3],plus(e[:3],e[3])

class Ring:
    def __init__(self,m): self.m=m; self.n=4*m; self.z=(0,)*self.n
    def clean(self,f):return {a:c for a,c in f.items() if c}
    def const(self,c):return {} if not c else {self.z:Q(c)}
    def var(self,i):a=list(self.z);a[i]=1;return {tuple(a):Q(1)}
    def add(self,*fs):
        out={}
        for f in fs:
            for a,c in f.items():out[a]=out.get(a,Q(0))+c
        return self.clean(out)
    def scale(self,c,f):return self.clean({a:Q(c)*b for a,b in f.items()})
    @lru_cache(maxsize=None)
    def redmon(self,a):
        k=next((4*c for c in range(self.m) if a[4*c]>=2),None)
        if k is None:return ((a,1),)
        b=list(a);b[k]-=2;out=dict(self.redmon(tuple(b)))
        for j in (1,2,3):
            c=b[:];c[k+j]+=2
            for d,t in self.redmon(tuple(c)):out[d]=out.get(d,0)-t
        return tuple((d,t) for d,t in out.items() if t)
    def reduce(self,f):
        out={}
        for a,c in f.items():
            for b,t in self.redmon(a):out[b]=out.get(b,Q(0))+c*t
        return self.clean(out)
    def mul(self,f,g):
        out={}
        for a,c in f.items():
            for b,d in g.items():
                ex=tuple(x+y for x,y in zip(a,b));out[ex]=out.get(ex,Q(0))+c*d
        return self.reduce(out)
    def derivative(self,f,i):
        out={}
        for a,c in f.items():
            if a[i]:b=list(a);b[i]-=1;out[tuple(b)]=a[i]*c
        return out
    @staticmethod
    @lru_cache(maxsize=None)
    def moment4(a):
        if any(x%2 for x in a):return Q(0)
        num=1;den=1
        for d in a:
            for k in range(1,d,2):num*=k
        for k in range(sum(a)//2):den*=4+2*k
        return Q(num,den)
    def mean(self,f):
        ans=Q(0)
        for a,c in f.items():
            for j in range(self.m):c*=self.moment4(a[4*j:4*j+4])
            ans+=c
        return ans
    def inner(self,f,g):
        ans=Q(0)
        for a,c in f.items():
            for b,d in g.items():
                z=c*d
                for j in range(self.m):z*=self.moment4(tuple(a[4*j+k]+b[4*j+k] for k in range(4)))
                ans+=z
        return ans
    def linear_field(self,f,terms):
        # A term (target-coordinate, multiplier-coordinate, coefficient)
        out={}
        for a,c in f.items():
            for i,j,t in terms:
                if a[i]:
                    b=list(a);b[i]-=1;b[j]+=1;b=tuple(b)
                    out[b]=out.get(b,Q(0))+c*a[i]*t
        return self.reduce(out)

def left_right_terms(chord,axis,right=False):
    # Quaternion generators T_alpha=-i sigma_alpha/2.
    off=4*chord;a=axis+1;terms=[(off,off+a,-Q(1,2)),(off+a,off,Q(1,2))]
    for b in range(1,4):
        for c in range(1,4):
            if len({a,b,c})==3:
                eps=1 if (a,b,c) in ((1,2,3),(2,3,1),(3,1,2)) else -1
                # (e_a cross q)_b=epsilon_(b,a,c) q_c
                terms.append((off+b,off+c,Q(eps if right else -eps,2)))
    return terms

class Cluster:
    def __init__(self,faces):
        self.faces=tuple(sorted(faces));self.edges=tuple(sorted(set().union(*(face_edges(p) for p in self.faces))))
        self.vertices=tuple(sorted(set(v for e in self.edges for v in endpoints(e))))
        unique=[sorted(e for e in face_edges(p) if sum(e in face_edges(q) for q in self.faces)==1) for p in self.faces]
        rank=len(self.edges)-len(self.vertices)+1
        found=None
        choices=product(*unique) if rank==len(self.faces) and all(unique) else ()
        if not choices: choices=()
        fallback=sorted(combinations(self.edges,rank),key=lambda ch:(sum(e in face_edges(f) for e in ch for f in self.faces),ch))
        from itertools import chain
        for chords in chain(choices,fallback):
            if len(set(chords))!=len(chords):continue
            tree=tuple(e for e in self.edges if e not in chords)
            if len(tree)!=len(self.vertices)-1:continue
            adj=defaultdict(list)
            for e in tree:
                u,v=endpoints(e);adj[u].append((v,e));adj[v].append((u,e))
            root=min(self.vertices);paths={root:frozenset()};stack=[root]
            while stack:
                u=stack.pop()
                for v,e in adj[u]:
                    if v not in paths:paths[v]=paths[u]|{e};stack.append(v)
            if len(paths)==len(self.vertices):found=(chords,tree,paths);break
        if found is None:raise ValueError('No spanning-tree gauge with one distinct face chord')
        self.chords,self.tree,self.paths=found;self.ring=R=Ring(len(self.chords));self.fields=[]
        for e in self.edges:
            row=[]
            for a in range(3):
                terms=[]
                if e in self.chords:terms+=left_right_terms(self.chords.index(e),a)
                else:
                    for j,c in enumerate(self.chords):
                        u,v=endpoints(c)
                        if e in self.paths[u]:terms+=left_right_terms(j,a)
                        if e in self.paths[v]:terms +=[(i,k,-t) for i,k,t in left_right_terms(j,a,True)]
                combo=defaultdict(Q)
                for i,j,c in terms:combo[(i,j)]+=c
                row.append(tuple((i,j,c) for (i,j),c in combo.items() if c))
            self.fields.append(tuple(row))
        def qmul(a,b):
            w,x,y,z=a;v,r,t,u=b
            return [R.add(R.mul(w,v),R.scale(-1,R.add(R.mul(x,r),R.mul(y,t),R.mul(z,u)))),
                    R.add(R.mul(w,r),R.mul(x,v),R.mul(y,u),R.scale(-1,R.mul(z,t))),
                    R.add(R.mul(w,t),R.scale(-1,R.mul(x,u)),R.mul(y,v),R.mul(z,r)),
                    R.add(R.mul(w,u),R.mul(x,t),R.scale(-1,R.mul(y,r)),R.mul(z,v))]
        def word(p):
            n=p[:3];i,j=p[3:]
            return [(n+(i,),1),(plus(n,i)+(j,),1),(plus(n,j)+(i,),-1),(n+(j,),-1)]
        self.W=[]
        for p in self.faces:
            a=[R.const(1),{},{},{}]
            for e,sgn in word(p):
                if e in self.chords:
                    j=self.chords.index(e);b=[R.var(4*j+k) for k in range(4)]
                    if sgn==-1:b=[b[0]]+[R.scale(-1,x) for x in b[1:]]
                    a=qmul(a,b)
            self.W.append(R.scale(2,a[0]))
        self.S=R.add(*self.W)
    def K(self,f):
        R=self.ring;pieces=[]
        for fields in self.fields:
            for terms in fields:
                if terms:pieces.append(R.linear_field(R.linear_field(f,terms),terms))
        return R.scale(-1,R.add(*pieces))
    def candidates(self,n=None,counts=None):
        energies=set()
        choices=combinations_with_replacement(self.faces,n) if counts is None else [tuple(p for p,k in zip(self.faces,counts) for _ in range(k))]
        for faces in choices:
            mult=[sum(e in face_edges(f) for f in faces) for e in self.edges]
            es={Q(0)}
            for m in mult:
                vals=[Q(k*(k+2),4) for k in range(m%2,m+1,2)]
                es={x+y for x in es for y in vals}
            energies.update(es)
        return sorted(energies-{0})
    def inv(self,f,n=None,counts=None):
        R=self.ring;f=R.add(f,R.const(-R.mean(f)));rem=f;out={}
        for c in self.candidates(n,counts):
            out=R.add(out,R.scale(1/c,rem));rem=R.add(rem,R.scale(-1/c,self.K(rem)))
        if rem:raise ArithmeticError(('candidate-spectrum-incomplete',len(rem)))
        if R.add(self.K(out),R.scale(-1,f)):raise ArithmeticError('inverse-residual')
        return out
    def multi_source(self,target):
        """Return exact coefficient of prod face-couplings^target in Q_H log psi."""
        R=self.ring;zero=(0,)*len(target)
        indices=sorted(product(*(range(k+1) for k in target)),key=lambda z:(sum(z),z))
        u={zero:R.const(1)};energy={zero:Q(0)};logu={};v={}
        leq=lambda a,b:all(x<=y for x,y in zip(a,b))
        minus=lambda a,b:tuple(x-y for x,y in zip(a,b))
        for nu in indices[1:]:
            forcing={}
            for i,k in enumerate(nu):
                if k:
                    mu=list(nu);mu[i]-=1
                    forcing=R.add(forcing,R.mul(self.W[i],u[tuple(mu)]))
            energy[nu]=-R.mean(forcing)
            f=forcing
            for mu,e in energy.items():
                if mu!=zero and mu!=nu and e and leq(mu,nu):
                    f=R.add(f,R.scale(e,u[minus(nu,mu)]))
            u[nu]=self.inv(f,counts=nu)
            # Euler equation: degree(u)=degree(log u)*u, preserving log constants.
            lg=u[nu]
            for mu,l in logu.items():
                if leq(mu,nu):
                    lg=R.add(lg,R.scale(-Q(sum(mu),sum(nu)),R.mul(l,u[minus(nu,mu)])))
            logu[nu]=lg;v[nu]=R.add(lg,R.const(-R.mean(lg)))
            # Independent original logarithmic-source equation on this exact coefficient.
            rhs={}
            if sum(nu)==1:rhs=self.W[nu.index(1)]
            else:
                for mu,l in v.items():
                    if mu!=nu and leq(mu,nu):
                        eta=minus(nu,mu)
                        if eta in v:
                            b=v[eta]
                            gamma=R.scale(Q(1,2),R.add(R.mul(self.K(l),b),R.mul(l,self.K(b)),R.scale(-1,self.K(R.mul(l,b)))))
                            rhs=R.add(rhs,gamma)
            rhs=R.add(rhs,R.const(-R.mean(rhs)))
            if R.add(self.K(v[nu]),R.scale(-1,rhs)):
                raise ArithmeticError(('logarithmic-source-failure',nu))
        return v[target],{'downset_coefficients':len(indices)-1,'spectral_inverse_checks':len(indices)-1,'logarithmic_source_checks':len(indices)-1,'intermediate_mean_checks':all(R.mean(u[k])==0 for k in u if k!=zero),'mean':str(R.mean(v[target]))}
    def sixth(self):
        R=self.ring;u1=self.inv(self.S,1);e2=-R.inner(self.S,u1)
        f2=R.mul(self.S,u1);u2=self.inv(f2,2)
        f3=R.add(R.mul(self.S,u2),R.scale(e2,u1));u3=self.inv(f3,3)
        e4=-R.inner(self.S,u3)
        e6=-R.inner(u3,self.K(u3))-e4*R.inner(u1,u1)-e2*R.inner(u2,u2)
        # independent same e6 from complete Rayleigh numerator and denominator
        N2=R.inner(u1,self.K(u1))-2*R.inner(self.S,u1)
        N4=R.inner(u2,self.K(u2))+2*R.inner(u1,self.K(u3))-2*R.inner(self.S,u3)-2*R.inner(u1,R.mul(self.S,u2))
        N6=R.inner(u3,self.K(u3))-2*R.inner(u2,R.mul(self.S,u3))
        den2=R.inner(u1,u1);den4=R.inner(u2,u2)+2*R.inner(u1,u3)
        if (N2,N4-e2*den2,N6-e4*den2-e2*den4)!=(e2,e4,e6):raise ArithmeticError('Rayleigh-identity')
        return {'faces':[list(p) for p in self.faces],'original_edges':len(self.edges),'vertices':len(self.vertices),'chords':[list(e) for e in self.chords], 'coefficients':[str(e2),str(e4),str(e6)],'polynomial_terms':[len(u1),len(u2),len(u3)],'means':[str(R.mean(x)) for x in [u1,u2,u3]],'inverse_residuals':'zero as exact sphere-quotient polynomials'}

if __name__=='__main__':
    import time,json
    samples={'single':[(0,0,0,0,1)],'adjacent':[(0,0,0,0,1),(1,0,0,0,1)],'path':[(0,0,0,0,1),(1,0,0,0,1),(2,0,0,0,1)],'common':[(0,0,0,0,1),(0,-1,0,0,1),(0,0,0,0,2)],'corner':[(0,0,0,0,1),(0,0,0,0,2),(0,0,0,1,2)]}
    for name,fs in samples.items():
        start=time.monotonic();c=Cluster(fs);ans=c.sixth();ans.update(type=name,seconds=time.monotonic()-start);print(json.dumps(ans),flush=True)
