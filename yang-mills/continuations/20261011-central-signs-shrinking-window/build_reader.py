from pathlib import Path
import re

def escape(text):
    replacements = {'\\': '\\textbackslash{}', '&': '\\&', '%': '\\%', '$': '\\$', '#': '\\#', '_': '\\_', '{': '\\{', '}': '\\}', '~': '\\textasciitilde{}', '^': '\\textasciicircum{}'}
    return ''.join((replacements.get(c, c) for c in text))
tokens = re.compile('(?s)(\\\\\\[.*?\\\\\\]|\\\\\\(.*?\\\\\\)|\\[[^\\]]*\\]\\([^)]+\\))')

def typeset_math(text):
    # Keep every formula character; aligned permits the multiple alignment
    # columns already present in the retained Markdown equations.
    text = text.replace(r'\begin{split}', r'\begin{aligned}').replace(r'\end{split}', r'\end{aligned}')
    text = re.sub(r'(\\begin\{(?:aligned|gathered)\})(\s*\[)', r'\1\\relax\2', text)
    # A new row's literal bracket is not an optional row-height argument.
    text = re.sub(r'(\\\\[ \t]*\n[ \t]*)(\[)', r'\1{}\2', text)
    def place_tag(match):
        block = match.group()
        tags = list(re.finditer(r'\\tag\{[^}]+\}', block))
        if len(tags) != 1:
            return block
        tag = tags[0]
        prefix = block[:tag.start()]
        depth = len(re.findall(r'\\begin\{', prefix)) - len(re.findall(r'\\end\{', prefix))
        if depth:
            prefix = prefix + '{}' if prefix.endswith('\\ ') else prefix.rstrip(' \t')
            block = prefix + block[tag.end():]
            block = block[:-2].rstrip() + '\n' + tag.group() + '\n' + block[-2:]
        return block
    return re.sub(r'(?s)\\\[.*?\\\]', place_tag, text)

def inline(text):
    output = []
    cursor = 0
    for match in tokens.finditer(text):
        output.append(escape(text[cursor:match.start()]))
        item = match.group()
        if item.startswith('\\'):
            output.append(item)
        else:
            m = re.fullmatch('\\[([^\\]]*)\\]\\(([^)]*)\\)', item)
            target = m.group(2)
            if not re.match('^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                target = globals().get('source_base_url', '') + target
            output.append('\\href{' + target + '}{' + escape(m.group(1)) + '}')
        cursor = match.end()
    output.append(escape(text[cursor:]))
    return ''.join(output)

def convert(text):
    mathblocks = []

    def keep(match):
        mathblocks.append(match.group())
        return '@@DISPLAY' + str(len(mathblocks) - 1) + '@@'
    text = re.sub('(?s)\\\\\\[.*?\\\\\\]|\\\\\\(.*?\\\\\\)', keep, text)
    text = re.sub('(?s)(!?\\[[^\\]]*\\]\\([^)]+\\))', lambda match: ' '.join(match.group().splitlines()), text)
    out = []
    table = False
    for line in text.splitlines():
        if line.startswith('|') and not line.startswith('||'):
            if re.fullmatch('\\|[\\s:|\\-]+\\|', line):
                continue
            if not table:
                columns = len(line.strip('|').split('|'))
                cell = 'p{\\dimexpr(\\linewidth-6pt*' + str(columns-1) + ')/' + str(columns) + '\\relax}'
                out.append('\\begingroup\\small\\setlength{\\tabcolsep}{3pt}\\begin{longtable}{@{}' + cell*columns + '@{}}\\toprule')
                table = True
            out.append(' & '.join((inline(x.strip()) for x in line.strip('|').split('|'))) + '\\\\')
            continue
        if table:
            out.append('\\bottomrule\\end{longtable}\\endgroup')
            table = False
        if line.startswith('!['):
            figure = re.fullmatch('!\\[([^\\]]*)\\]\\(([^)]+)\\)', line)
            if figure is None:
                raise ValueError('Unparsed figure: ' + line)
            out.append('\\begin{figure}[htbp]\\centering\\includegraphics[width=\\linewidth,height=.72\\textheight,keepaspectratio]{' + figure.group(2) + '}\\caption{' + inline(figure.group(1)) + '}\\end{figure}')
        elif line.startswith('## '):
            out.append('\\subsection*{' + escape(line[3:]) + '}')
        elif line.startswith('# '):
            out.append('\\section*{' + escape(line[2:]) + '}')
        elif re.fullmatch('@@DISPLAY\\d+@@', line):
            block = mathblocks[int(line[9:-2])]
            if re.search('\\\\tag\\{(?:PK25|PK132|PK158)\\}', block):
                out.append('\\begingroup\\footnotesize' + '\n' + block + '\n' + '\\endgroup')
            else:
                out.append(block)
        else:
            line = re.sub('\\*\\*([^*]*)\\*\\*', '\\1', line)
            out.append(inline(line))
    if table:
        out.append('\\bottomrule\\end{longtable}\\endgroup')
    return typeset_math(re.sub('@@DISPLAY(\\d+)@@', lambda match: mathblocks[int(match.group(1))], '\n'.join(out)))
HEADER = '\\documentclass[11pt]{article}\n\\usepackage{iftex}\n\\ifPDFTeX\\usepackage[T1]{fontenc}\\usepackage[utf8]{inputenc}\\usepackage{lmodern}\\else\\usepackage{fontspec}\\setmainfont{Latin Modern Roman}\\fi\n\\usepackage{amsmath,amssymb,mathrsfs,booktabs,graphicx,hyperref}\n\\usepackage[margin=21.5mm]{geometry}\n\\hypersetup{hidelinks,pdftitle={Yang--Mills: complete research proofs}}\n\\allowdisplaybreaks\n\\emergencystretch=3em\n\\setlength{\\parindent}{0pt}\n\\setlength{\\parskip}{6pt}\n\\begin{document}\n'

import json,hashlib
ROOT=Path(__file__).resolve().parent
source_base_url='https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/'
names=json.loads((ROOT/'READER_SOURCES.json').read_text(encoding='utf-8'))
rows=[];bodies=[]
for name in names:
    p=ROOT/name;s=p.read_text(encoding='utf-8')
    source_base_url='https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/'+(p.parent.relative_to(ROOT).as_posix()+'/' if p.parent!=ROOT else '')
    body=convert(s)
    if name in ['ACTUAL_MIXED_TIME_EVOLUTION.md', 'ACTUAL_RESOLVENT_HESSIAN.md', 'CENTRAL_KINETIC_SOURCE.md', 'SIGNED_RESIDUAL_RESPONSE.md']:
        heading=r'\subsection*{Both original mixed sources and the entire inverse tail}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['SIGNED_RESIDUAL_RESPONSE.md', 'CENTRAL_KINETIC_SOURCE.md', 'CENTRAL_FLUCTUATION_ENERGY.md', 'POSITIVE_TIME_COVARIANCE.md']:
        heading=r'\subsection*{Actual memory and complete character-coordinate operator}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['ACTUAL_RESOLVENT_HESSIAN.md', 'CENTRAL_KINETIC_SOURCE.md', 'CENTRAL_FLUCTUATION_ENERGY.md', 'CENTRAL_FIXED_POINT_RESIDUAL.md', 'ACTUAL_LOW_ENERGY_MAPS.md', 'union_label_global/FULL_UNION_LABEL_INVERSE.md']:
        heading=r'\subsection*{Full differentiated residual and original scalar overlap}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['ACTUAL_HESSIAN_BOUNDS.md', 'CENTRAL_HESSIAN_FACE_MAP.md', 'CENTRAL_KINETIC_SOURCE.md', 'CENTRAL_FLUCTUATION_ENERGY.md', 'CENTRAL_FIXED_POINT_RESIDUAL.md', 'HESSIAN_RECEIVING_REVIEW.md']:
        heading=r'\subsection*{Actual resolvent derivatives and explicit residual gain}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['CENTRAL_HESSIAN_FACE_MAP.md', 'CENTRAL_KINETIC_SOURCE.md', 'CENTRAL_FLUCTUATION_ENERGY.md', 'CENTRAL_FIXED_POINT_RESIDUAL.md', 'HESSIAN_RECEIVING_REVIEW.md', 'POTENTIAL_VARIANCE_IDENTITIES.md']:
        heading=r'\subsection*{Actual conditional Hessian bounds and complete response terms}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['CENTRAL_KINETIC_SOURCE.md', 'CENTRAL_FLUCTUATION_ENERGY.md', 'CENTRAL_FIXED_POINT_RESIDUAL.md', 'GAUGE_HESSIAN_AND_COVARIANT_GRAPH.md', 'SCALAR_COMMON_SOURCE_RECONSTRUCTION.md', 'ACTUAL_DENSITY_CHARACTERS.md']:
        heading=r'\subsection*{Actual central Hessians and their full original face maps}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['CENTRAL_KINETIC_SOURCE.md', 'CENTRAL_FLUCTUATION_ENERGY.md', 'ACTUAL_DENSITY_CHARACTERS.md', 'SCALAR_COMMON_SOURCE_RECONSTRUCTION.md', 'CONDITIONAL_GROUND_CURRENT_TRIAL.md']:
        heading=r'\subsection*{Central configurations and strict physical resolvent gain}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['CENTRAL_KINETIC_SOURCE.md', 'ACTUAL_DENSITY_CHARACTERS.md', 'FACE_FIELD_PHYSICAL_ACTION.md', 'SCALAR_COMMON_SOURCE_RECONSTRUCTION.md', 'CONDITIONAL_GROUND_CURRENT_TRIAL.md']:
        heading=r'\subsection*{Exact central fluctuation energy and full response residual}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['ACTUAL_DENSITY_CHARACTERS.md', 'FACE_FIELD_PHYSICAL_ACTION.md', 'SCALAR_COMMON_SOURCE_RECONSTRUCTION.md', 'CONDITIONAL_GROUND_CURRENT_TRIAL.md', 'BOUNDED_ENERGY_MULTIPLIER.md']:
        heading=r'\subsection*{Central kinetic source and complete physical resolvent}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['FACE_FIELD_PHYSICAL_ACTION.md', 'SCALAR_RESIDUAL_AND_LOCAL_ENERGY.md', 'SCALAR_COMMON_SOURCE_RECONSTRUCTION.md', 'CENTRAL_SIGNS_AND_BOUNDARIES.md']:
        heading=r'\subsection*{Actual density characters and central-reversal spectral weight}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['SCALAR_RESIDUAL_AND_LOCAL_ENERGY.md', 'SHARED_FACE_WORDS_AND_PHYSICAL_COUPLING.md', 'CENTRAL_SIGNS_AND_BOUNDARIES.md']:
        heading=r'\subsection*{Face action and the exact ground-density receiver}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['SCALAR_COMMON_SOURCE_RECONSTRUCTION.md', 'SMOOTH_WEIGHTED_LOCAL_ENERGY.md', 'SHARED_FACE_WORDS_AND_PHYSICAL_COUPLING.md', 'ACTUAL_EDGE_ENERGY_VARIANCE.md']:
        heading=r'\subsection*{Scalar residual and original local-energy moments}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['TWO_FORM_FORCE_AND_COMMON_SPECTRUM.md', 'ACTUAL_PHYSICAL_SCORE_SPECTRAL_MEASURE.md', 'PHYSICAL_SCALAR_RECEIVER_AND_CURRENT_COVARIANCE.md', 'FULL_CURRENT_SCHUR_AND_ENERGY_MEASURE.md', 'POSITIVE_TIME_COVARIANCE.md', 'ACTUAL_GROUND_GRADIENT_TRIAL.md', 'ACTUAL_KINETIC_PROFILE_AND_SHIFT_MOMENTS.md', 'GAUGE_HESSIAN_AND_COVARIANT_GRAPH.md']:
        heading=r'\subsection*{Exact scalar source and full positive-energy band}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name == 'TWO_FORM_FORCE_AND_COMMON_SPECTRUM.md':
        heading=r'\subsection*{Reproducible diagnostics and illustrations}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['GAUGE_CURRENT_COVARIANCE_AND_DYNAMIC_CURL.md', 'GAUGE_HESSIAN_AND_COVARIANT_GRAPH.md', 'ACTUAL_PHYSICAL_SCORE_SPECTRAL_MEASURE.md', 'PHYSICAL_SCALAR_RECEIVER_AND_CURRENT_COVARIANCE.md', 'FULL_CURRENT_SCHUR_AND_ENERGY_MEASURE.md', 'ACTUAL_KINETIC_PROFILE_AND_SHIFT_MOMENTS.md', 'ACTUAL_GROUND_GRADIENT_TRIAL.md', 'CURRENT_DENSITY_FLUX_AND_PROJECTED_RESIDUAL.md', 'QUANTITATIVE_FORCE_CURL.md', 'POSITIVE_TIME_COVARIANCE.md']:
        heading=r'\subsection*{Exact force receiver and common physical source}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name == 'GAUGE_CURRENT_COVARIANCE_AND_DYNAMIC_CURL.md':
        heading=r'\subsection*{Reproducible figure and diagnostics}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['GAUGE_HESSIAN_AND_COVARIANT_GRAPH.md', 'ACTUAL_PHYSICAL_SCORE_SPECTRAL_MEASURE.md', 'PHYSICAL_SCALAR_RECEIVER_AND_CURRENT_COVARIANCE.md', 'FULL_CURRENT_SCHUR_AND_ENERGY_MEASURE.md', 'ACTUAL_KINETIC_PROFILE_AND_SHIFT_MOMENTS.md', 'ACTUAL_GROUND_GRADIENT_TRIAL.md', 'CURRENT_DENSITY_FLUX_AND_PROJECTED_RESIDUAL.md', 'QUANTITATIVE_FORCE_CURL.md', 'POSITIVE_TIME_COVARIANCE.md']:
        heading=r'\subsection*{Full gauge-current matrix and exact dynamic curl}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name == 'GAUGE_HESSIAN_AND_COVARIANT_GRAPH.md':
        heading=r'\subsection*{Reproducible figure and diagnostics}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['PHYSICAL_SCALAR_RECEIVER_AND_CURRENT_COVARIANCE.md', 'FULL_CURRENT_SCHUR_AND_ENERGY_MEASURE.md', 'ACTUAL_KINETIC_PROFILE_AND_SHIFT_MOMENTS.md', 'ACTUAL_GROUND_GRADIENT_TRIAL.md', 'CURRENT_DENSITY_FLUX_AND_PROJECTED_RESIDUAL.md', 'ACTUAL_PHYSICAL_SCORE_SPECTRAL_MEASURE.md', 'CENTERED_CURRENT_COVARIANCE.md', 'ACTUAL_SCORE_MOMENTS_AND_SECOND_ENERGY.md']:
        heading=r'\subsection*{Original gauge constraints and stronger actual-state bounds}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name == 'ACTUAL_PHYSICAL_SCORE_SPECTRAL_MEASURE.md':
        heading=r'\subsection*{Reproducible figure and diagnostics}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['PHYSICAL_SCALAR_RECEIVER_AND_CURRENT_COVARIANCE.md', 'FULL_CURRENT_SCHUR_AND_ENERGY_MEASURE.md', 'ACTUAL_KINETIC_PROFILE_AND_SHIFT_MOMENTS.md', 'ACTUAL_GROUND_GRADIENT_TRIAL.md', 'CURRENT_DENSITY_FLUX_AND_PROJECTED_RESIDUAL.md']:
        heading=r'\subsection*{Actual physical spectral measure and its total kernel}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['FULL_CURRENT_SCHUR_AND_ENERGY_MEASURE.md', 'ACTUAL_KINETIC_PROFILE_AND_SHIFT_MOMENTS.md', 'ACTUAL_GROUND_GRADIENT_TRIAL.md', 'CURRENT_DENSITY_FLUX_AND_PROJECTED_RESIDUAL.md', 'CENTERED_CURRENT_COVARIANCE.md', 'ACTUAL_SCORE_MOMENTS_AND_SECOND_ENERGY.md', 'HESSIAN_RECEIVING_REVIEW.md']:
        heading=r'\subsection*{Exact physical scalar receiver and stronger original-state bounds}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name == 'FULL_CURRENT_SCHUR_AND_ENERGY_MEASURE.md':
        body=body.replace('The plotted block model is a specified diagnostic',r'\clearpage'+'\nThe plotted block model is a specified diagnostic')
    if name in ['ACTUAL_KINETIC_PROFILE_AND_SHIFT_MOMENTS.md', 'EXACT_PATCH_GREEN_AND_PHYSICAL_RECEIVER.md', 'CURRENT_DENSITY_FLUX_AND_PROJECTED_RESIDUAL.md', 'ACTUAL_GROUND_GRADIENT_TRIAL.md', 'POSITIVE_TIME_COVARIANCE.md']:
        heading=r'\subsection*{Full current complement and its relative-energy measure}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['EXACT_PATCH_GREEN_AND_PHYSICAL_RECEIVER.md', 'CURRENT_DENSITY_FLUX_AND_PROJECTED_RESIDUAL.md', 'CENTERED_CURRENT_COVARIANCE.md', 'ACTUAL_GROUND_GRADIENT_TRIAL.md', 'ACTUAL_SCORE_MOMENTS_AND_SECOND_ENERGY.md']:
        heading=r'\subsection*{Actual kinetic profiles and joint shift moments}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['QUANTITATIVE_FORCE_CURL.md', 'CURRENT_DENSITY_FLUX_AND_PROJECTED_RESIDUAL.md', 'TWO_SIDED_CURRENT_RESIDUAL.md', 'THREE_SHIFT_GAINS_AND_SOURCE_GRAPH.md']:
        heading=r'\subsection*{Exact source Green limit and physical inverse receiver}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['QUANTITATIVE_FORCE_CURL.md', 'CURRENT_DENSITY_FLUX_AND_PROJECTED_RESIDUAL.md', 'TWO_SIDED_CURRENT_RESIDUAL.md', 'CENTERED_CURRENT_COVARIANCE.md', 'ACTUAL_SCORE_MOMENTS_AND_SECOND_ENERGY.md']:
        heading=r'\subsection*{Joint source graph and spatial force bounds}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['CURRENT_DENSITY_FLUX_AND_PROJECTED_RESIDUAL.md', 'TWO_SIDED_CURRENT_RESIDUAL.md', 'ACTUAL_GROUND_GRADIENT_TRIAL.md', 'CENTERED_CURRENT_COVARIANCE.md']:
        heading=r'\subsection*{Quantitative force curl on the original patch}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['CENTERED_CURRENT_COVARIANCE.md', 'TWO_SIDED_CURRENT_RESIDUAL.md', 'ACTUAL_GROUND_GRADIENT_TRIAL.md', 'ACTUAL_FILTERED_CURRENT_AND_TAIL.md', 'CURRENT_TAILS_AND_RETAINED_SOURCE.md']:
        heading=r'\subsection*{Exact density flux and stronger physical residual}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['ACTUAL_GROUND_GRADIENT_TRIAL.md', 'ACTUAL_SCORE_MOMENTS_AND_SECOND_ENERGY.md', 'CURRENT_TAILS_AND_RETAINED_SOURCE.md', 'TWO_SIDED_CURRENT_RESIDUAL.md', 'SIMULTANEOUS_CENTRAL_MEASURE.md']:
        heading=r'\subsection*{Positive current measures and individual plaquette means}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['ACTUAL_FILTERED_CURRENT_AND_TAIL.md', 'CURRENT_TAILS_AND_RETAINED_SOURCE.md', 'ORIGINAL_SOURCE_HESSIAN_AND_FILTER.md', 'ORDERED_WILSON_ACTION.md']:
        heading=r'\subsection*{Complete residual and exact stereographic current}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['BOUNDED_ENERGY_MULTIPLIER.md', 'ACTUAL_FILTERED_CURRENT_AND_TAIL.md', 'CURRENT_TAILS_AND_RETAINED_SOURCE.md', 'FULL_PHYSICAL_LIFT_AND_SOURCE.md']:
        heading=r'\subsection*{Original source Hessian and the stronger full-source response}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['ACTUAL_SCORE_MOMENTS_AND_SECOND_ENERGY.md', 'ACTUAL_FILTERED_CURRENT_AND_TAIL.md', 'ACTUAL_GROUND_GRADIENT_TRIAL.md', 'CURRENT_COVARIANCE_EQUALITY.md', 'ENERGY_ROOT_AND_ANCHORED_HISTORIES.md']:
        heading=r'\subsection*{Stronger source energy and retained current inverses}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['BOUNDED_ENERGY_MULTIPLIER.md', 'ACTUAL_GROUND_GRADIENT_TRIAL.md', 'ACTUAL_FILTERED_CURRENT_AND_TAIL.md']:
        heading=r'\subsection*{Actual score moments and the full second-energy matrix}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['FULL_PHYSICAL_LIFT_AND_SOURCE.md', 'POSITIVE_TIME_COVARIANCE.md', 'ACTUAL_GROUND_GRADIENT_TRIAL.md']:
        heading=r'\subsection*{Actual filtered currents and the complete inverse contribution}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['FULL_HAMILTONIAN_GROUND_FIBER.md', 'RAW_OVERLAP_AND_ORIGINAL_METRIC.md']:
        heading=r'\subsection*{Full physical lift and original-source spectral windows}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['ACTUAL_EDGE_ENERGY_VARIANCE.md', 'SMOOTH_WEIGHTED_LOCAL_ENERGY.md', 'LOCAL_CURVATURE_BUDGET.md']:
        heading=r'\subsection*{Full ground-family coupling and positive actual raw overlap}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['SMOOTH_WEIGHTED_LOCAL_ENERGY.md','SHARED_FACE_WORDS_AND_PHYSICAL_COUPLING.md','LOCAL_CURVATURE_BUDGET.md']:
        heading=r'\subsection*{Actual-vacuum edge variance and surrounding-loop energy}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['SMOOTH_WEIGHTED_LOCAL_ENERGY.md','CONDITIONAL_GROUND_CURRENT_TRIAL.md','LOCAL_CURVATURE_BUDGET.md']:
        heading=r'\subsection*{Shared-face physical coupling and the complete exterior state}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['LOCAL_ENERGY_PHYSICAL_WINDOWS.md','ACTUAL_GROUND_GRADIENT_TRIAL.md','OUTSIDE_FORCE_AND_CURRENT_MOMENTS.md']:
        heading=r'\subsection*{Smooth spatial energy and exact sector covariances}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['KINETIC_CURRENT_AND_PHYSICAL_ENERGY.md', 'INSIDE_MARGINAL_ENERGY.md']:
        heading=r'\subsection*{Complete local energy and physical spectral windows}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name == 'BOUNDARY_DIVERGENCE_AND_MARGINAL_MOMENTS.md':
        heading=r'\subsection*{Original kinetic current and its full physical energy}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['BOUNDARY_FORCE_PROJECTION.md', 'CONDITIONAL_GROUND_CURRENT_TRIAL.md']:
        heading=r'\subsection*{Boundary divergence and marginal second moments}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name == 'ACTUAL_GROUND_GRADIENT_TRIAL.md':
        heading=r'\subsection*{Exact boundary projection and actual current-moment bounds}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name == 'OUTSIDE_FORCE_AND_CURRENT_MOMENTS.md':
        heading=r'\subsection*{Exact boundary projection and actual current-moment bounds}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name == 'RETAINED_DERIVATIVE_AND_GOOD_BOUNDARIES.md':
        heading=r'\subsection*{Conditional outside forcing and current moments}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name == 'CONDITIONAL_GROUND_CURRENT_TRIAL.md':
        heading=r'\subsection*{Retained derivatives and actual good boundary cubes}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['ACTUAL_GROUND_GRADIENT_TRIAL.md', 'BOUNDED_ENERGY_MULTIPLIER.md']:
        heading=r'\subsection*{Conditional ground currents and independent fluctuation weights}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name in ['POSITIVE_TIME_COVARIANCE.md', 'CURRENT_COVARIANCE_EQUALITY.md']:
        heading=r'\subsection*{Actual ground-gradient trials and complete variational residual}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    if name == 'ENERGY_ROOT_AND_ANCHORED_HISTORIES.md':
        # Flush the existing full-page figure before the new receiving note.
        heading=r'\subsection*{Positive-time covariance and the full resolvent tail}'
        body=body.replace(heading,r'\clearpage'+'\n'+heading)
    blocks=re.findall(r'(?s)\\\[.*?\\\]|\\\(.*?\\\)',s)
    assert all(typeset_math(x) in body for x in blocks)
    rows.append({'source':name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'complete_math_blocks':len(blocks),'split_to_aligned_wrappers':s.count(r'\begin{split}')})
    if name in ['NEGATIVE_TRACE_COMPRESSION.md', 'GAMMA_INTEGRAL.md', 'HOLONOMY_CURVATURE_RECEIVING.md', 'HOLONOMY_CURVATURE_REVIEW.md', 'SIMULTANEOUS_CENTRAL_MEASURE.md', 'CURRENT_COVARIANCE_EQUALITY.md', 'SMOOTH_MEASURE_REALIZATION.md', 'AMPLITUDE_ALGEBRA.md', 'GLOBAL_MEASURE_EVOLUTION.md', 'STATIONARY_PHASE_RECEIVING.md', 'ENERGY_ROOT_AND_ANCHORED_HISTORIES.md', 'POSITIVE_TIME_COVARIANCE.md', 'ACTUAL_GROUND_GRADIENT_TRIAL.md', 'CONDITIONAL_GROUND_CURRENT_TRIAL.md', 'RETAINED_DERIVATIVE_AND_GOOD_BOUNDARIES.md', 'WILSON_AND_CURRENT_COVARIANCE_SIGNS.md', 'OUTSIDE_FORCE_AND_CURRENT_MOMENTS.md', 'BOUNDARY_FORCE_PROJECTION.md', 'BOUNDARY_DIVERGENCE_AND_MARGINAL_MOMENTS.md', 'KINETIC_CURRENT_AND_PHYSICAL_ENERGY.md', 'LOCAL_ENERGY_PHYSICAL_WINDOWS.md', 'SMOOTH_WEIGHTED_LOCAL_ENERGY.md', 'SHARED_FACE_WORDS_AND_PHYSICAL_COUPLING.md', 'ACTUAL_EDGE_ENERGY_VARIANCE.md', 'FULL_HAMILTONIAN_GROUND_FIBER.md', 'RAW_OVERLAP_AND_ORIGINAL_METRIC.md', 'FULL_PHYSICAL_LIFT_AND_SOURCE.md', 'ACTUAL_FILTERED_CURRENT_AND_TAIL.md', 'ACTUAL_SCORE_MOMENTS_AND_SECOND_ENERGY.md', 'CURRENT_TAILS_AND_RETAINED_SOURCE.md', 'ORIGINAL_SOURCE_HESSIAN_AND_FILTER.md', 'TWO_SIDED_CURRENT_RESIDUAL.md', 'STEREOGRAPHIC_CURRENT_AND_CUBIC.md', 'CENTERED_CURRENT_COVARIANCE.md', 'CURRENT_DENSITY_FLUX_AND_PROJECTED_RESIDUAL.md', 'QUANTITATIVE_FORCE_CURL.md', 'THREE_SHIFT_GAINS_AND_SOURCE_GRAPH.md', 'EXACT_PATCH_GREEN_AND_PHYSICAL_RECEIVER.md', 'ACTUAL_KINETIC_PROFILE_AND_SHIFT_MOMENTS.md', 'FULL_CURRENT_SCHUR_AND_ENERGY_MEASURE.md', 'PHYSICAL_SCALAR_RECEIVER_AND_CURRENT_COVARIANCE.md', 'ACTUAL_PHYSICAL_SCORE_SPECTRAL_MEASURE.md', 'GAUGE_HESSIAN_AND_COVARIANT_GRAPH.md', 'GAUGE_CURRENT_COVARIANCE_AND_DYNAMIC_CURL.md', 'TWO_FORM_FORCE_AND_COMMON_SPECTRUM.md', 'SCALAR_COMMON_SOURCE_RECONSTRUCTION.md', 'SCALAR_RESIDUAL_AND_LOCAL_ENERGY.md', 'FACE_FIELD_PHYSICAL_ACTION.md', 'ACTUAL_DENSITY_CHARACTERS.md', 'CENTRAL_KINETIC_SOURCE.md', 'CENTRAL_FLUCTUATION_ENERGY.md', 'CENTRAL_FIXED_POINT_RESIDUAL.md', 'CENTRAL_HESSIAN_FACE_MAP.md', 'ACTUAL_HESSIAN_BOUNDS.md', 'ACTUAL_RESOLVENT_HESSIAN.md', 'SIGNED_RESIDUAL_RESPONSE.md', 'ACTUAL_MIXED_TIME_EVOLUTION.md', 'MIXED_SOURCE_OPERATOR_ACTION.md']:
        body='\\begingroup\\ifPDFTeX\\else\\IfFontExistsTF{Cambria}{\\fontspec{Cambria}}{\\IfFontExistsTF{DejaVu Sans}{\\fontspec{DejaVu Sans}}{}}\\fi\n'+body+'\n\\endgroup'
    bodies.append(body)
header=HEADER.replace('Yang--Mills: complete research proofs','Yang--Mills central signs and shrinking spectral windows').replace('booktabs,graphicx','booktabs,longtable,graphicx')
out=ROOT/'RESEARCH_CONTINUATION.tex'
out.write_text(header+'\n\\clearpage\n'.join(bodies)+'\n\\end{document}\n',encoding='utf-8',newline='\n')
(ROOT/'TEX_FIDELITY.json').write_text(json.dumps({'sources':rows,'all_math_blocks_preserved':True,
 'typesetting_map':'Split wrappers become aligned; inert relax and empty groups protect leading and new-row square brackets; a tag inside an inner alignment moves outside that alignment. Equation content and tags are retained. Tables retain all cells with their actual column count. Markdown set-delimiter corrections are recorded separately in the source-fidelity receipt.',
 'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'compilation_confirmed':False,
 'compile_status':'Compilation has not been confirmed for this source edition; no current PDF is included.'},indent=2)+'\n')
print(json.dumps({'math_blocks':sum(x['complete_math_blocks'] for x in rows),'source_files':len(rows)}))
