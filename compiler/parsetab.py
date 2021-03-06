
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftplusminusandorand boolean cbracket ccurly cparen dedent doublequal else equals identifier if indent input integer minus nequal newline not obracket ocurly oparen or plus print string whilemodule : statement_liststatement_list : newline statementstatement_list : newline statement newline statement_liststatement_list : statement newline statement_liststatement_list : statement newlinestatement_list : statement statement_liststatement_list : statementstatement : expressionsuite : statement newline\n            | newline indent statement_list dedentstatement : if expression ":" suite else ":" suitestatement : while expression ":" suitestatement : identifier equals expressionexpression : oparen expression cparenexpression : expression doublequal expressionexpression : expression nequal expressionexpression : expression and expressionexpression : expression or expressionexpression : plus expressionexpression : minus expressionexpression : not expressionstatement : print expressionexpression : expression plus expressionexpression : expression minus expressionexpression : inputexpression : integer\n                    | booleanexpression : identifier'
    
_lr_action_items = {'doublequal':([2,8,10,14,15,17,18,21,22,24,25,26,34,38,41,42,43,44,45,46,47,],[-27,-25,-26,-28,28,-28,28,28,28,28,28,-19,-20,-14,28,28,-17,28,-24,-23,-18,]),'and':([2,8,10,14,15,17,18,21,22,24,25,26,34,38,41,42,43,44,45,46,47,],[-27,-25,-26,-28,29,-28,29,29,29,29,29,-19,-20,-14,29,29,-17,29,-24,-23,-18,]),'boolean':([0,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,19,22,24,26,27,28,29,30,31,32,33,34,35,36,38,39,40,41,42,43,44,45,46,47,51,53,54,56,58,60,61,],[2,-27,2,2,2,2,2,-25,2,-26,2,2,-28,-8,2,-28,2,-22,-21,-19,2,2,2,2,2,2,2,-20,2,2,-14,2,2,-13,-15,-17,-16,-24,-23,-18,2,-12,-9,2,2,-11,-10,]),'if':([0,2,4,7,8,10,14,15,17,19,22,24,26,34,35,36,38,39,40,41,42,43,44,45,46,47,51,53,54,56,58,60,61,],[3,-27,3,3,-25,-26,-28,-8,-28,3,-22,-21,-19,-20,3,3,-14,3,3,-13,-15,-17,-16,-24,-23,-18,3,-12,-9,3,3,-11,-10,]),'cparen':([2,8,10,17,21,24,26,34,38,42,43,44,45,46,47,],[-27,-25,-26,-28,38,-21,-19,-20,-14,-15,-17,-16,-24,-23,-18,]),'oparen':([0,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,19,22,24,26,27,28,29,30,31,32,33,34,35,36,38,39,40,41,42,43,44,45,46,47,51,53,54,56,58,60,61,],[5,-27,5,5,5,5,5,-25,5,-26,5,5,-28,-8,5,-28,5,-22,-21,-19,5,5,5,5,5,5,5,-20,5,5,-14,5,5,-13,-15,-17,-16,-24,-23,-18,5,-12,-9,5,5,-11,-10,]),'print':([0,2,4,7,8,10,14,15,17,19,22,24,26,34,35,36,38,39,40,41,42,43,44,45,46,47,51,53,54,56,58,60,61,],[6,-27,6,6,-25,-26,-28,-8,-28,6,-22,-21,-19,-20,6,6,-14,6,6,-13,-15,-17,-16,-24,-23,-18,6,-12,-9,6,6,-11,-10,]),'input':([0,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,19,22,24,26,27,28,29,30,31,32,33,34,35,36,38,39,40,41,42,43,44,45,46,47,51,53,54,56,58,60,61,],[8,-27,8,8,8,8,8,-25,8,-26,8,8,-28,-8,8,-28,8,-22,-21,-19,8,8,8,8,8,8,8,-20,8,8,-14,8,8,-13,-15,-17,-16,-24,-23,-18,8,-12,-9,8,8,-11,-10,]),':':([2,8,10,17,18,24,25,26,34,38,42,43,44,45,46,47,55,],[-27,-25,-26,-28,35,-21,40,-19,-20,-14,-15,-17,-16,-24,-23,-18,58,]),'$end':([1,2,4,8,10,13,14,15,17,19,20,22,23,24,26,34,36,37,38,41,42,43,44,45,46,47,51,52,53,54,57,60,61,],[0,-27,-7,-25,-26,-1,-28,-8,-28,-5,-6,-22,-2,-21,-19,-20,-2,-4,-14,-13,-15,-17,-16,-24,-23,-18,-5,-3,-12,-9,-3,-11,-10,]),'dedent':([2,4,8,10,14,15,17,19,20,22,23,24,26,34,36,37,38,41,42,43,44,45,46,47,51,52,53,54,57,59,60,61,],[-27,-7,-25,-26,-28,-8,-28,-5,-6,-22,-2,-21,-19,-20,-2,-4,-14,-13,-15,-17,-16,-24,-23,-18,-5,-3,-12,-9,-3,61,-11,-10,]),'newline':([0,2,4,8,10,14,15,17,19,22,23,24,26,34,35,36,38,39,40,41,42,43,44,45,46,47,48,51,53,54,56,58,60,61,],[7,-27,19,-25,-26,-28,-8,-28,7,-22,39,-21,-19,-20,50,51,-14,7,50,-13,-15,-17,-16,-24,-23,-18,54,7,-12,-9,7,50,-11,-10,]),'nequal':([2,8,10,14,15,17,18,21,22,24,25,26,34,38,41,42,43,44,45,46,47,],[-27,-25,-26,-28,30,-28,30,30,30,30,30,-19,-20,-14,30,30,-17,30,-24,-23,-18,]),'equals':([14,],[27,]),'else':([49,54,61,],[55,-9,-10,]),'not':([0,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,19,22,24,26,27,28,29,30,31,32,33,34,35,36,38,39,40,41,42,43,44,45,46,47,51,53,54,56,58,60,61,],[9,-27,9,9,9,9,9,-25,9,-26,9,9,-28,-8,9,-28,9,-22,-21,-19,9,9,9,9,9,9,9,-20,9,9,-14,9,9,-13,-15,-17,-16,-24,-23,-18,9,-12,-9,9,9,-11,-10,]),'integer':([0,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,19,22,24,26,27,28,29,30,31,32,33,34,35,36,38,39,40,41,42,43,44,45,46,47,51,53,54,56,58,60,61,],[10,-27,10,10,10,10,10,-25,10,-26,10,10,-28,-8,10,-28,10,-22,-21,-19,10,10,10,10,10,10,10,-20,10,10,-14,10,10,-13,-15,-17,-16,-24,-23,-18,10,-12,-9,10,10,-11,-10,]),'indent':([50,],[56,]),'minus':([0,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,38,39,40,41,42,43,44,45,46,47,51,53,54,56,58,60,61,],[16,-27,16,16,16,16,16,-25,16,-26,16,16,-28,31,16,-28,31,16,31,31,31,31,-19,16,16,16,16,16,16,16,-20,16,16,-14,16,16,31,31,-17,31,-24,-23,-18,16,-12,-9,16,16,-11,-10,]),'while':([0,2,4,7,8,10,14,15,17,19,22,24,26,34,35,36,38,39,40,41,42,43,44,45,46,47,51,53,54,56,58,60,61,],[11,-27,11,11,-25,-26,-28,-8,-28,11,-22,-21,-19,-20,11,11,-14,11,11,-13,-15,-17,-16,-24,-23,-18,11,-12,-9,11,11,-11,-10,]),'plus':([0,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,38,39,40,41,42,43,44,45,46,47,51,53,54,56,58,60,61,],[12,-27,12,12,12,12,12,-25,12,-26,12,12,-28,32,12,-28,32,12,32,32,32,32,-19,12,12,12,12,12,12,12,-20,12,12,-14,12,12,32,32,-17,32,-24,-23,-18,12,-12,-9,12,12,-11,-10,]),'identifier':([0,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,19,22,24,26,27,28,29,30,31,32,33,34,35,36,38,39,40,41,42,43,44,45,46,47,51,53,54,56,58,60,61,],[14,-27,17,14,17,17,14,-25,17,-26,17,17,-28,-8,17,-28,14,-22,-21,-19,17,17,17,17,17,17,17,-20,14,14,-14,14,14,-13,-15,-17,-16,-24,-23,-18,14,-12,-9,14,14,-11,-10,]),'or':([2,8,10,14,15,17,18,21,22,24,25,26,34,38,41,42,43,44,45,46,47,],[-27,-25,-26,-28,33,-28,33,33,33,33,33,-19,-20,-14,33,33,-17,33,-24,-23,-18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement_list':([0,4,19,36,39,51,56,],[13,20,37,20,52,57,59,]),'suite':([35,40,58,],[49,53,60,]),'expression':([0,3,4,5,6,7,9,11,12,16,19,27,28,29,30,31,32,33,35,36,39,40,51,56,58,],[15,18,15,21,22,15,24,25,26,34,15,41,42,43,44,45,46,47,15,15,15,15,15,15,15,]),'statement':([0,4,7,19,35,36,39,40,51,56,58,],[4,4,23,36,48,4,4,48,36,4,48,]),'module':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> module","S'",1,None,None,None),
  ('module -> statement_list','module',1,'p_module','parser.py',11),
  ('statement_list -> newline statement','statement_list',2,'p_statement_list_nl_begin','parser.py',16),
  ('statement_list -> newline statement newline statement_list','statement_list',4,'p_statement_list_nl_begin_middle','parser.py',20),
  ('statement_list -> statement newline statement_list','statement_list',3,'p_statement_list_nl','parser.py',24),
  ('statement_list -> statement newline','statement_list',2,'p_statement_nl','parser.py',29),
  ('statement_list -> statement statement_list','statement_list',2,'p_statement_nl2','parser.py',33),
  ('statement_list -> statement','statement_list',1,'p_statement','parser.py',38),
  ('statement -> expression','statement',1,'p_statement_expression','parser.py',43),
  ('suite -> statement newline','suite',2,'p_suite','parser.py',48),
  ('suite -> newline indent statement_list dedent','suite',4,'p_suite','parser.py',49),
  ('statement -> if expression : suite else : suite','statement',7,'p_statement_if','parser.py',57),
  ('statement -> while expression : suite','statement',4,'p_statement_while','parser.py',61),
  ('statement -> identifier equals expression','statement',3,'p_name_equals','parser.py',65),
  ('expression -> oparen expression cparen','expression',3,'p_parens','parser.py',70),
  ('expression -> expression doublequal expression','expression',3,'p_compare_equals','parser.py',75),
  ('expression -> expression nequal expression','expression',3,'p_compare_nequals','parser.py',79),
  ('expression -> expression and expression','expression',3,'p_compare_and','parser.py',83),
  ('expression -> expression or expression','expression',3,'p_compare_or','parser.py',87),
  ('expression -> plus expression','expression',2,'p_unaryadd','parser.py',92),
  ('expression -> minus expression','expression',2,'p_unarysub','parser.py',97),
  ('expression -> not expression','expression',2,'p_unarynot','parser.py',101),
  ('statement -> print expression','statement',2,'p_print_statement','parser.py',106),
  ('expression -> expression plus expression','expression',3,'p_plus_expression','parser.py',111),
  ('expression -> expression minus expression','expression',3,'p_sub_expression','parser.py',116),
  ('expression -> input','expression',1,'p_input_expression','parser.py',121),
  ('expression -> integer','expression',1,'p_intbool_expression','parser.py',127),
  ('expression -> boolean','expression',1,'p_intbool_expression','parser.py',128),
  ('expression -> identifier','expression',1,'p_name','parser.py',132),
]
