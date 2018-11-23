from AST import *


def get_variable_name():
    global TEMP_COUNT
    variable_name = "tmp_" + str(TEMP_COUNT)
    TEMP_COUNT = TEMP_COUNT + 1
    return variable_name

TEMP_COUNT = 0
ATOMIC     = 0
BINDINGS   = 1

def flatten_ast(stmts):
    if isinstance(stmts, Module):
        return Module(None, flatten_ast(stmts.node))
    elif isinstance(stmts, Stmt):
        return Stmt([y for x in stmts.nodes for y in flatten_stmt(x)])


def flatten_stmt(s):
    if isinstance(s, Printnl):
        [atomic, bindings] = flatten_expr(s.nodes[0])
        return bindings + [Printnl([atomic], s.dest)]
    elif isinstance(s, CallFunc):
        return flatten_expr(s)[1]
    elif isinstance(s, Assign):
        atomic_n = s.nodes
        bindings_n = []
        [atomic_e, bindings_e] = flatten_expr(s.expr)
        return bindings_e + bindings_n + [Assign(atomic_n, atomic_e)]
    elif isinstance(s, Discard):
        [atomic, bindings] = flatten_expr(s.expr)
        return bindings + [Discard(atomic)]
    elif isinstance(s, If):
        then = flatten_ast(s.then)
        else_ = flatten_ast(s.else_)
        [atomic, bindings] = flatten_expr(s.tests)
        return bindings + [If(atomic, then, else_)]
    elif isinstance(s, While):
        body = flatten_ast(s.body)
        [atomic, bindings] = flatten_expr(s.tests)
        return bindings + [While(atomic, body)]
    else:
        print s
        raise Exception('unrecognized statement node %s' % s)


def flatten_expr(n):
    def make_assign(lhs, rhs):
        return Assign([AssName(lhs, 'OP_ASSIGN')], rhs)

    def atomic_bindings(flat_expr, bindings):
        var = get_variable_name()
        return [Name(var), bindings + [make_assign(var, flat_expr)]]

    if isinstance(n, Assign):
        res = flatten_expr(n.expr)
        if isinstance(n.nodes[0], AssName):
            return res[BINDINGS] + [Assign(n.nodes, res[ATOMIC])]
        else:
            flat_nodes = flatten_expr(n.nodes[0])
            return res[BINDINGS] + [Assign(flat_nodes, res[ATOMIC])]
    elif isinstance(n, AssName):
        return [n, []]
    elif isinstance(n, Const):
        return [n, []]
    elif isinstance(n, Name):
        return [n, []]
    elif isinstance(n, Box):
        typ = n.typ
        (atomic, bindings) = flatten_expr(n.arg)
        return atomic_bindings(Box(typ, atomic),bindings)
    elif isinstance(n, Unbox):
        typ = n.typ
        (atomic, bindings) = flatten_expr(n.arg)
        return atomic_bindings(Unbox(typ, atomic),bindings)
    elif isinstance(n, Add):
        (atomic_l, bindings_l) = flatten_expr(n.left)
        (atomic_r, bindings_r) = flatten_expr(n.right)
        return atomic_bindings(Add((atomic_l, atomic_r)), bindings_l + bindings_r)
    elif isinstance(n, Sub):
        (atomic_l, bindings_l) = flatten_expr(n.left)
        (atomic_r, bindings_r) = flatten_expr(n.right)
        return atomic_bindings(Sub((atomic_l, atomic_r)), bindings_l + bindings_r)
    elif isinstance(n, UnarySub):
        (atomic, bindings) = flatten_expr(n.expr)
        return atomic_bindings(UnarySub(atomic), bindings)
    elif isinstance(n, Not):
        (atomic, bindings) = flatten_expr(n.expr)
        return atomic_bindings(Not(atomic), bindings)
    elif isinstance(n, UnaryAdd):
        (atomic, bindings) = flatten_expr(n.expr)
        return atomic_bindings(UnaryAdd(atomic), bindings)
    elif isinstance(n, CallFunc):
        flat_args = []
        bindings = []
        if n.args:
            for a in n.args:
                flat_a = flatten_expr(a)
                flat_args.append(flat_a[ATOMIC])
                bindings = bindings + flat_a[BINDINGS]
        # (atomic_n, atomic_binding) = flatten_expr(n.node)
        # bindings += atomic_binding
        return atomic_bindings(CallFunc(n.node, flat_args, None, None), bindings)
    elif isinstance(n, If):
        (flat_test, test_a) = flatten_expr(n.tests)
        (flat_then, then_a) = flatten_expr(n.then)
        (flat_else, else_a) = flatten_expr(n.else_)
        temp = get_variable_name()

        bindings = test_a + [If(flat_test, \
                                then_a + [make_assign(temp, flat_then)], \
                                    else_a + [make_assign(temp, flat_else)])]
        return [Name(temp), bindings]

    elif isinstance(n, Equals):
        (atomic_l, bindings_l) = flatten_expr(n.left)
        (atomic_r, bindings_r) = flatten_expr(n.right)
        return atomic_bindings(Equals((atomic_l, atomic_r)), bindings_l + bindings_r)

    elif isinstance(n, NotEquals):
        (atomic_l, bindings_l) = flatten_expr(n.left)
        (atomic_r, bindings_r) = flatten_expr(n.right)
        return atomic_bindings(NotEquals((atomic_l, atomic_r)), bindings_l + bindings_r)

    else:
        print
        print n
        print
        raise Exception('Error in flatten_expr: unrecognized AST node')