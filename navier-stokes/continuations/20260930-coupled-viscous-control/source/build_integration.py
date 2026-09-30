"""Export the complete proof body for integration into the cumulative TeX.

No mathematics is abridged. Every label and its internal references acquire
the prefix cvlane: to avoid collisions. No source project is written.
"""
from pathlib import Path
import hashlib
import json
import re
import shutil

HERE=Path(__file__).resolve().parent
OUT=HERE/'integration'
OUT.mkdir(exist_ok=True)
inputs=[
    'physical_realization.tex',
    'finite_stage/first_stage_section.tex',
    'finite_stage/evolving_diffusive_parent_section.tex',
    'finite_stage/actual_viscous_entry.tex',
    'second_return/second_return_body.tex',
    'modified_spatial/modified_spatial_body.tex',
    'third_growth_geometry/third_growth_geometry_body.tex',
    'finite_stage/third_growth_entry.tex',
    'third_transition/third_transition_body.tex',
    'third_growth_spatial/third_growth_spatial_body.tex',
    'third_transition_spatial/third_transition_spatial_body.tex',
    'third_return/third_return_body.tex',
    'third_return/third_return_completion_body.tex',
    'third_return/local_spatial_body.tex',
    'coupled_feedback.tex',
    'infinite_status.tex',
    'infinite_modified/parabolic_similarity_body.tex',
    'infinite_modified/based_cascade_body.tex',
    'infinite_modified/return_correction_body.tex',
    'infinite_modified/full_support_force_body.tex',
    'infinite_modified/force_reachability_body.tex',
    'paper_coupling/coupled_background_body.tex',
    'paper_coupling/profile_diffusion/profile_diffusion_body.tex',
]
parts=[]
for rel in inputs:
    content=(HERE/rel).read_text(encoding='utf-8-sig')
    if rel=='paper_coupling/coupled_background_body.tex':
        content='\\section{Full source controls and aggregate background identities}\n'+content
    if rel.endswith('profile_diffusion_body.tex'):
        content=content.replace('\\section','\\subsection')
        content='\\section{Exact periodic profile evolution and the affine region}\n'+content
    parts.append('% Complete source: '+rel+'\n'+content)
body='\n\n'.join(parts)
labels=re.findall(r'\\label\{([^}]+)\}',body)
if len(labels)!=len(set(labels)):
    raise RuntimeError('Duplicate labels in full source body')
for command in ('label','ref','eqref','pageref'):
    body=re.sub(r'\\'+command+r'\{([^}]+)\}',
                lambda m:'\\'+command+'{cvlane:'+m.group(1)+'}',body)
body=re.sub(r'\\hyperref\[([^\]]+)\]',
            lambda m:'\\hyperref[cvlane:'+m.group(1)+']',body)
for old,new in [('proposition','cvlaneproposition'),('lemma','cvlanlemma'),
                ('theorem','cvlanetheorem'),
                ('pdproposition','cvlanepdproposition')]:
    body=body.replace('\\begin{'+old+'}', '\\begin{'+new+'}')
    body=body.replace('\\end{'+old+'}', '\\end{'+new+'}')
(OUT/'coupled_viscous_control_body.tex').write_text(body,encoding='utf-8')
preamble=r'''% Load before \begin{document}; full body has no document wrapper.
\RequirePackage{amsmath,amssymb,amsthm,mathtools,mathrsfs,longtable,hyperref,graphicx}
\providecommand{\R}{\mathbb R}
\providecommand{\AB}{\mathrm{AB}}
\providecommand{\epsv}{\varepsilon_{\mathrm v}}
\providecommand{\kapth}{\kappa_{\mathrm{th}}}
\providecommand{\Gcal}{\mathcal G}
\providecommand{\dd}{\mathrm d}
\providecommand{\tr}{\operatorname{tr}}
\providecommand{\sym}{\operatorname{sym}}
\providecommand{\PDReal}{\mathbb R}
\providecommand{\PDTorus}{\mathbb T}
\providecommand{\PDd}{\mathrm d}
\providecommand{\PDthermal}{\kappa_{\rm th}}
\providecommand{\PDviscosity}{\nu_{\rm phys}}
\providecommand{\PDheat}{\mathcal H}
\providecommand{\PDmean}[1]{\langle #1\rangle}
\newtheorem{cvlaneproposition}{Proposition}
\newtheorem{cvlanlemma}{Lemma}
\newtheorem{cvlanetheorem}{Theorem}
\newtheorem{cvlanepdproposition}{Proposition}
'''
(OUT/'coupled_viscous_control_preamble.tex').write_text(preamble,encoding='utf-8')
figure_source=HERE/'third_return/figures/third_return_persistence.png'
figure_output=OUT/'third_return/figures/third_return_persistence.png'
figure_output.parent.mkdir(parents=True,exist_ok=True)
shutil.copy2(figure_source,figure_output)
similarity_figure_source=HERE/'infinite_modified/figures/fixed_diffusion_similarity.png'
similarity_figure_output=OUT/'infinite_modified/figures/fixed_diffusion_similarity.png'
similarity_figure_output.parent.mkdir(parents=True,exist_ok=True)
shutil.copy2(similarity_figure_source,similarity_figure_output)
based_figure_source=HERE/'infinite_modified/figures/based_cascade_residual.png'
based_figure_output=OUT/'infinite_modified/figures/based_cascade_residual.png'
based_figure_output.parent.mkdir(parents=True,exist_ok=True)
shutil.copy2(based_figure_source,based_figure_output)
return_figure_source=HERE/'infinite_modified/figures/return_correction.png'
return_figure_output=OUT/'infinite_modified/figures/return_correction.png'
return_figure_output.parent.mkdir(parents=True,exist_ok=True)
shutil.copy2(return_figure_source,return_figure_output)
full_force_source=HERE/'infinite_modified/figures/full_support_force.png'
full_force_output=OUT/'infinite_modified/figures/full_support_force.png'
full_force_output.parent.mkdir(parents=True,exist_ok=True)
shutil.copy2(full_force_source,full_force_output)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=dict(schema='coupled-viscous-control-integration-v1',
    primary_source=dict(title='Blowup for the Boussinesq equations with smooth forcing',
                        authors=['Levent Alpöge','Tristan Buckmaster'],pages=76,
                        url='https://cims.nyu.edu/~tristanb/boussinesq.pdf',
                        file='sources/alpoge_buckmaster_boussinesq.pdf',
                        sha256=sha(HERE/'sources/alpoge_buckmaster_boussinesq.pdf')),
    complete_body='integration/coupled_viscous_control_body.tex',
    preamble='integration/coupled_viscous_control_preamble.tex',
    assets=[dict(source='third_return/figures/third_return_persistence.png',
                 integration='integration/third_return/figures/third_return_persistence.png',
                 sha256=sha(figure_source)),
            dict(source='infinite_modified/figures/fixed_diffusion_similarity.png',
                 integration='integration/infinite_modified/figures/fixed_diffusion_similarity.png',
                 sha256=sha(similarity_figure_source)),
            dict(source='infinite_modified/figures/based_cascade_residual.png',
                 integration='integration/infinite_modified/figures/based_cascade_residual.png',
                 sha256=sha(based_figure_source)),
            dict(source='infinite_modified/figures/return_correction.png',
                 integration='integration/infinite_modified/figures/return_correction.png',
                 sha256=sha(return_figure_source)),
            dict(source='infinite_modified/figures/full_support_force.png',
                 integration='integration/infinite_modified/figures/full_support_force.png',
                 sha256=sha(full_force_source))],
    input_sections=[dict(file=r,sha256=sha(HERE/r)) for r in inputs],
    output_files_sha256={p.name:sha(p) for p in OUT.glob('*.tex')},
    label_prefix='cvlane:',label_count=len(labels),
    abridged=False,document_wrapper=False,
    mathematics_scope='Complete compact forced first stage; three actual original growth targets, evolved-parent second return and hold, full third transition with revived second parent, complete third shooting family and selected return on a definite positive equal-diffusion interval, and compact profile forces; pressure-independent obstruction for the unchanged released infinite state; exact transfer of the finite return to every radius at fixed positive physical diffusion; raw-copy term obstruction and force-flat jet space; complete-packet reset obstruction; signed based-increment residual arrays and state interface; exact full chart transition and affine-state orbit classification; actual triangular returned core and positive horizontal temperature gradient; explicit unforced affine continuation and compact flat core correction; complete signed full-support force and all mixed jets with explicit cutoff constants; quantitative annulus diffusion lower bounds and exact cancellation-defect maps. The all-stage force budget, next full-profile return map and corrected infinite trajectory remain unproved.',
    source_estimate_attribution='Source infinite existence and induction bounds remain explicitly attributed; not independently re-proved as new results.',
    infinite_viscous_sequence_proved=False)
(HERE/'integration_manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(dict(exported_sections=len(inputs),labels=len(labels),abridged=False)))
