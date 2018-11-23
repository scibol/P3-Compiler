import ply.yacc as yacc
from AST import *
import sys
from scanner import tokens

precedence = (
    ('left', 'plus', 'minus', 'and', 'or'),
)

def p_module(t):
    'module : statement_list'
    t[0] = Module(None, Stmt(t[1]))


def p_statement_list_nl_begin(t):
    'statement_list : newline statement'
    t[0] = [t[2]]

def p_statement_list_nl_begin_middle(t):
    'statement_list : newline statement newline statement_list'
    t[0] = [t[2]] + t[4]

def p_statement_list_nl(t):
    'statement_list : statement newline statement_list'
    t[0] = [t[1]] + t[3]


def p_statement_nl(t):
    'statement_list : statement newline'
    t[0] = [t[1]]

def p_statement_nl2(t):
    'statement_list : statement statement_list'
    t[0] = [t[1]] + t[2]


def p_statement(t):
    'statement_list : statement'
    t[0] = [t[1]]


def p_statement_expression(t):
    'statement : expression'
    t[0] = Discard(t[1])


def p_suite(t):
    '''suite : statement newline
            | newline indent statement_list dedent'''
    if len(t) == 1:
        t[0] = [t[1]]
    else:
        t[0] = t[3]


def p_statement_if(t):
    'statement : if expression ":" suite else ":" suite'
    t[0] = If(t[2], Stmt(t[4]), Stmt(t[7]))

def p_statement_while(t):
    'statement : while expression ":" suite'
    t[0] = While(t[2], Stmt(t[4]))

def p_name_equals(t):
    'statement : identifier equals expression'
    t[0] = Assign([AssName(t[1], 'OP_ASSIGN')], t[3])


def p_parens(t):
    'expression : oparen expression cparen'
    t[0] = t[2]

# def p_compare(t):
#     '''expression : expression doublequal expression
#                     | expression nequal expression'''
#     if (t[2] == "=="):
#         t[0] =


def p_compare_equals(t):
    'expression : expression doublequal expression'
    t[0] = Equals([t[1], t[3]])

def p_compare_nequals(t):
    'expression : expression nequal expression'
    t[0] = NotEquals([t[1], t[3]])

def p_compare_and(t):
    'expression : expression and expression'
    t[0] = And([t[1], t[3]])

def p_compare_or(t):
    'expression : expression or expression'
    t[0] = Or([t[1], t[3]])


def p_unaryadd(t):
    'expression : plus expression'
    t[0] = UnaryAdd(t[2])


def p_unarysub(t):
    'expression : minus expression'
    t[0] = UnarySub(t[2])

def p_unarynot(t):
    'expression : not expression'
    t[0] = Not(t[2])


def p_print_statement(t):
    'statement : print expression'
    t[0] = Printnl([t[2]], None)


def p_plus_expression(t):
    'expression : expression plus expression'
    t[0] = Add((t[1], t[3]))


def p_sub_expression(t):
    'expression : expression minus expression'
    t[0] = Sub((t[1], t[3]))


def p_input_expression(t):
    'expression : input'
    t[0] = CallFunc(Name('input'), [], None, None)



def p_intbool_expression(t):
    '''expression : integer
                    | boolean'''
    t[0] = Const(t[1])

def p_name(t):
    'expression : identifier'
    t[0] = Name(t[1])



def p_error(t):
    raise SyntaxError


def parseFile(path):
    parser = yacc.yacc()
    input_file = open(path, "r")
    s = input_file.read()
    try:
        result = parser.parse(s)
        input_file.close()
        return result
    except:
        input_file.close()
        sys.exit(1)
