import ply.lex as lex

states = (
    ('indent', 'exclusive'),
    ('dedent', 'exclusive'),
    ('comment', 'exclusive'),
    ('main', 'exclusive')
)

tokens = [
    'indent', 'dedent', 'identifier', 'newline',
    'oparen', 'cparen', 'obracket', 'cbracket', 'ocurly', 'ccurly',
    'string', 'integer', 'input', 'boolean'
]

t_indent_ignore = ''
t_dedent_ignore = ''

def t_indent_error(t):
    pass

def t_dedent_error(t):
    pass

def t_comment_error(t):
    pass

def t_error(t):
    pass

def t_comment_skip(t):
    r'[^\n]+'
    pass

def t_ANY_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    if len(t.lexer.paren_stack) == 0:
        t.lexer.curr_indent = 0
        if t.lexer.lexstate != 'indent':
            t.lexer.begin('indent')
            return t

def t_main_softnewline(t):
    r'\\\n'
    t.lexer.lineno += 1

def t_indent_comment(t):
    r'\#'
    t.lexer.begin('comment')

def char_val(c):
    if c == ' ':
        return 1
    elif c == '\t':
        return 8
    else:
        return 0

def t_indent_ws(t):
    r'[ \t]+'
    t.lexer.curr_indent += sum(map(char_val, t.value))

def process_indent(lexer):
    cnt = 0
    curr = lexer.curr_indent
    topi = lexer.indents.pop()
    while topi > curr:
        topi = lexer.indents.pop()
        cnt += 1
    lexer.indents.append(topi)
    if topi == curr:
        return -cnt
    if topi < curr:
        if cnt == 0:
            return 1
        print "Indentation error: unexpected indentation level ", curr
        return -cnt

def t_indent_indent(t):
    r'[^ \#\t\n]'
    t.lexer.lexpos -= 1
    val = process_indent(t.lexer)
    if val == 0:
        t.lexer.begin('main')
    elif val < 0:
        t.lexer.begin('dedent')
        t.lexer.dedent_cnt = -val
    else:
        t.lexer.indents.append(t.lexer.curr_indent)
        t.lexer.begin('main')
        return t

def t_dedent_dedent(t):
    r'.'
    t.lexer.lexpos -= 1
    t.lexer.dedent_cnt -= 1
    if t.lexer.dedent_cnt == 0:
        t.lexer.begin('main')
    return t

invert_paren = {
    '(' : ')',
    '[' : ']',
    '{' : '}'
}

paren_token_name = {
    '(' : 'oparen',
    ')' : 'cparen',
    '[' : 'obracket',
    ']' : 'cbracket',
    '{' : 'ocurly',
    '}' : 'ccurly'
}

def t_main_open(t):
    r'[\(\[\{]'
    t.lexer.paren_stack.append(invert_paren[t.value])
    t.type = paren_token_name[t.value]
    return t

def t_main_close(t):
    r'[\)\]\}]'
    last = t.lexer.paren_stack.pop()
    if last != t.value:
        print "Unmatched", t.value
        t.lexer.paren_stack.append(last)
    t.type = paren_token_name[t.value]
    return t

def token_override(self):
    t = self.token_()
    if t is None:
        return process_eof(self)
    return t

def process_eof(lexer):
    if len(lexer.indents) == 1:
        return None
    lexer.indents.pop()

    tok = lex.LexToken()
    tok.value = ''
    tok.type = 'dedent'
    tok.lineno = lexer.lineno
    tok.lexpos = lexer.lexpos
    tok.lexer = lexer
    return tok

reserved = {
    'print' : 'print',
    'if' : 'if',
    'else' : 'else',
    'while' : 'while',
    'and' : 'and',
    'or' : 'or',
    'not' : 'not'
}

def process_string(string):
    # TODO: define me! (optional for P0, but need to do eventually)
    return string

def t_main_string_short_single(t):
    r"(r|R|UR|Ur|U|uR|ur|u|br|bR|b|BR|Br|B)?'[^'\n]*'"
    t.type = 'string'
    return process_string(t)

def t_main_string_short_double(t):
    r'(r|R|UR|Ur|U|uR|ur|u|br|bR|b|BR|Br|B)?"[^"\n]*"'
    t.type = 'string'
    return process_string(t)

literals = ".@,:`;~"

t_main_ignore = ' \t'

t_main_plus = r'\+'
t_main_minus = r'-'
t_main_doublequal = r'=='
t_main_nequal =r'!='
t_main_equals = r'='

tokens += ['plus', 'minus', 'doublequal', 'nequal', 'equals' ] + list(reserved.values())

def t_main_input(t):
    r'input\(\)'
    t.type = 'input'
    t.value = str(t.value)
    return t


def t_main_boolean(t):
    r'True|False'
    t.value = str(t.value)
    t.type = 'boolean'
    return t


def t_main_identifier(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'identifier')
    t.value = str(t.value)
    return t


def t_main_integer(t):
    r'\d+'
    t.value = int(t.value)
    t.type = 'integer'
    return t



def t_main_error(t):
    pass

def t_main_comment(t):
    '\#'
    t.lexer.begin('comment')


lexer = lex.lex()
lexer.indents = []
lexer.indents.append(0)
lexer.paren_stack = []
lexer.curr_indent = 0
lexer.token_ = lexer.token
lexer.token = (lambda: token_override(lexer))
lexer.begin('indent')

