from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json, time
from project_fifth import ROOT,Source,local_word,decode
from trace_algebra import gamma,multiply,trace,haar,add,scale

def main():
    start=time.monotonic()
    saved=json.loads((ROOT/'FIFTH_FACE_PROJECTIONS.json').read_text())
    rows=[]
    for row in saved['projected_rows']:
        src=Source(tuple(map(tuple,row['faces'])))
        cs=tuple(row['multiplicity'])
        wp=trace(local_word(tuple(row['output_face']),{'edge_coordinates':row['union_edges']}))
        pieces={}
        split_records=[]
        for degree in [1,2]:
            result=F(0)
            for mu in product(*(range(c+1) for c in cs)):
                if sum(mu)!=degree:continue
                nu=tuple(c-a for c,a in zip(cs,mu))
                expr=gamma(src.v(mu),src.v(nu))
                value=haar(multiply(wp,expr))
                result+=value
                split_records.append({'left':mu,'right':nu,'haar_gamma':str(value)})
            pieces[str(degree)+'_'+str(5-degree)]=result
        total=F(2,3)*sum(pieces.values())
        assert total==F(row['projection']),row['index']
        out={'index':row['index'],'classification':row['classification'],
             'output_face':row['output_face'],'source_faces':row['faces'],
             'pieces':{k:str(v) for k,v in pieces.items()},
             'coefficient_factor':'2/3','projection':str(total),'all_original_splits':split_records}
        rows.append(out)
        print(row['index'],row['classification'],out['pieces'],total,round(time.monotonic()-start,2),flush=True)
        Source.v.cache_clear()
        Source.spectrum.cache_clear()
    (ROOT/'PROJECTED_RHS_REDERIVATION.json').write_text(json.dumps({'method':'Exact Haar of W_output times every original (1,4) and (2,3) Gamma split; original P K^-1=P/3 retained','rows':rows,'elapsed_seconds':time.monotonic()-start},indent=2)+'\n')

if __name__=='__main__':main()
