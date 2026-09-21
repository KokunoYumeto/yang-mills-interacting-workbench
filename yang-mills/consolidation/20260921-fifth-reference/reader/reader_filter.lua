-- Preserve literal source tokens while permitting line breaks in long notation.
function Code(el)
  if not FORMAT:match('latex') then return nil end
  local escape = {
    ['\\']='\\textbackslash{}', ['{']='\\{', ['}']='\\}',
    ['#']='\\#', ['$']='\\$', ['%']='\\%', ['&']='\\&',
    ['_']='\\_', ['^']='\\textasciicircum{}', ['~']='\\textasciitilde{}',
    ['<']='\\textless{}', ['>']='\\textgreater{}',
  }
  local parts = {}
  for _, cp in utf8.codes(el.text) do
    local char = utf8.char(cp)
    parts[#parts+1] = (escape[char] or char) .. '\\allowbreak{}'
  end
  return pandoc.RawInline('latex', '{\\ttfamily ' .. table.concat(parts) .. '}')
end

function Str(el)
  if not FORMAT:match('latex') then return nil end
  if #el.text < 18 then return nil end
  if not el.text:match('[_/<>]') and not el.text:match('^[a-f0-9]+[,%.]?$') then return nil end
  local result = Code(el)
  result.text = result.text:gsub('\\ttfamily ', '')
  return result
end

-- Scale only oversized display boxes; retain formula tokens and source labels.
-- split becomes aligned solely because the inner display is boxed for sizing.
function Math(el)
  if not FORMAT:match('latex') or el.mathtype ~= 'DisplayMath' then return nil end
  local tag = el.text:match('\\tag{([^}]+)}')
  local formula = el.text:gsub('\\tag{[^}]+}', '')
  formula = formula:gsub('{split}', '{aligned}')
  formula = formula:gsub('^%s+', ''):gsub('%s+$', ''):gsub('\n%s*\n', '\n')
  -- F38's source array omits its header row terminator before hline.
  -- Supply that typesetting-only separator; values and original bytes remain.
  formula = formula:gsub('below}\\hline', 'below}' .. string.rep('\\', 3) .. 'hline')
  local width = tag and '0.92\\linewidth' or '\\linewidth'
  local ending = tag and ('\\tag{' .. tag .. '}') or ''
  return pandoc.RawInline('latex', '\\begingroup\\small\\begin{equation*}\n' ..
    '\\adjustbox{max width=' .. width .. '}{$\\displaystyle ' .. formula .. '$}' ..
    ending .. '\n\\end{equation*}\\endgroup')
end
