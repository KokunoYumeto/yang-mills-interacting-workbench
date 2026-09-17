"""Build exact, fully expanded original-source fourth coefficients, one per orbit."""
from pathlib import Path
from collections import Counter
from fractions import Fraction as Q
import json,argparse,time,hashlib
from gauge_polynomial import Cluster
ROOT=Path(__file__).resolve().parents[1]

def serialize_poly(f):return [{'powers':list(a),'coefficient':str(c)} for a,c in sorted(f.items())]
def serialized_model(c):
 return {'faces':[list(f) for f in c.faces],'original_edges':[list(e) for e in c.edges],
         'original_tree':[list(e) for e in c.tree],'chords':[list(e) for e in c.chords],
         'root':list(min(c.vertices)),
         'tree_paths':[[list(v),[list(e) for e in sorted(p)]] for v,p in sorted(c.paths.items())],
         'left_right_fields':[[[[i,j,str(t)] for i,j,t in f] for f in row] for row in c.fields],
         'plaquette_polynomials':[serialize_poly(p) for p in c.W]}

def compute(k,entry):
 fs=[tuple(x) for x in entry['faces_with_multiplicity']];ps=tuple(sorted(set(fs)));nu=tuple(fs.count(x) for x in ps)
 c=Cluster(ps);start=time.monotonic();f,report=c.multi_source(nu)
 # Unit coupling coefficient = coefficient of this literal multivariate monomial.
 terms=serialize_poly(f)
 out={'index':k,'faces_with_multiplicity':[list(x) for x in fs],'coupling_multiindex':list(nu),
      'anchored_multiplicity':entry['anchored_multiplicity'],'partition':entry['partition'],
      'quaternion_coordinates':'(q0,q1,q2,q3) for each listed chord; q0^2=1-q1^2-q2^2-q3^2',
      'model':serialized_model(c),'coefficient_polynomial':terms,'symbolic_certificate':report,
      'nonzero':bool(f),'coefficient_Haar_mean':str(c.ring.mean(f)),
      'coefficient_Haar_squared_norm':str(c.ring.inner(f,f)),
      'coefficient_energy_Haar':str(c.ring.inner(f,c.K(f)))}
 info={'index':k,'seconds':time.monotonic()-start,'terms':len(f),'chords':len(c.chords)}
 return out,info

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--start',type=int,default=0);ap.add_argument('--end',type=int,default=78);args=ap.parse_args()
 entries=json.loads((ROOT/'results/quartic_geometric_classes.json').read_text())['classes'];outdir=ROOT/'results/quartic_coefficients';outdir.mkdir(exist_ok=True)
 log=ROOT/'logs/quartic_build.jsonl'
 for i in range(args.start,min(args.end,len(entries))):
  out,info=compute(i,entries[i]);raw=(json.dumps(out,sort_keys=True,indent=2)+'\n').encode();(outdir/f'class_{i:02d}.json').write_bytes(raw)
  info['sha256']=hashlib.sha256(raw).hexdigest()
  with log.open('a') as f:f.write(json.dumps(info,sort_keys=True)+'\n')
  print(json.dumps(info),flush=True)
if __name__=='__main__':main()
