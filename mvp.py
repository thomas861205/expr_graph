pnl = [10.0, 11.0, -2.0]
weight = [1, 2, 1]

UNIT_INDENT = ' ' * 2

class node:
  def __init__(self, v, isConst, lvl=0):
    self.v = v
    self.const = isConst
    self.lvl = lvl

def sum_opr(ls):
  ret = sum([ele.v if isinstance(ele, node) else node(ele, True).v
             for ele in ls])
  lvl = max([ele.lvl if isinstance(ele, node) else node(ele, True).lvl
             for ele in ls]) + 1
  txt = [f'+sum: {ret}\n']
  for ele in ls:
    if isinstance(ele, node):
      continue
    txt.append(UNIT_INDENT + f'+---- {ele}\n')
  return node(ret, False, lvl=lvl), txt

def square_opr():
  return

def abs_opr():
  return

def dump_text(txt_metas):
  lvl_ls = [meta[1] for meta in txt_metas]
  max_lvl = max(lvl_ls)
  unit_indent = ' ' * 2
  for txt_ls, lvl in reversed(txt_metas):
    indent_mult = max_lvl - lvl
    for txt in txt_ls:
      print(UNIT_INDENT * indent_mult + txt, end='')

def expr1():
  text_buffer = []
  spnl, txt1 = sum_opr(pnl)
  text_buffer.append((txt1, spnl.lvl))
  sweight, txt2 = sum_opr(weight)
  text_buffer.append((txt2, sweight.lvl))
  spw, txt3 = sum_opr([spnl, sweight])
  text_buffer.append((txt3, spw.lvl))
  print(spnl.lvl, sweight.lvl, spw.lvl)
  dump_text(text_buffer)

expr1()
