-- Preserve literal inline source notation while allowing long paths to wrap.
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

-- Plain-text source formulas and filenames are not necessarily marked as code.
-- Preserve their glyphs and Roman font, but permit line breaks inside long
-- uninterrupted tokens so the archival text cannot extend into the margin.
function Str(el)
  if not FORMAT:match('latex') then return nil end
  if #el.text < 18 or not el.text:match('[_/<>]') then return nil end
  local result = Code(el)
  result.text = result.text:gsub('\\ttfamily ', '')
  return result
end
