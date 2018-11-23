from AST import *
from assembly import *

TEMP_COUNT = 0
ATOMIC     = 0
BINDINGS   = 1


def mapVarToAddr(flatExprs):
    varToAddrMap = {}
    varNum = 1
    for flatExpr in flatExprs:
        if isinstance(flatExpr, Assign) and flatExpr.nodes[0].name not in varToAddrMap.keys():
            varToAddrMap[flatExpr.nodes[0].name] = "-" + str(varNum*4) + "(%ebp)"
            varNum = varNum + 1
    return varToAddrMap


def translate_to_x86(flatExprs):
    x86_stmts = []
    for flatExpr in flatExprs:
        if isinstance(flatExpr, Printnl):
            atomic = flatExpr.nodes[0]
            x86_stmts.append(Push(Name("%ecx")))
            x86_stmts.append(Push(Name("%edx")))
            x86_stmts.append(Push(Name("%eax")))
            x86_stmts.append(Push(atomic))
            x86_stmts.append(PrintX86(atomic))
            x86_stmts.append(Addl(Const(4), Name("%esp")))
            x86_stmts.append(Pop(Name("%eax")))
            x86_stmts.append(Pop(Name("%edx")))
            x86_stmts.append(Pop(Name("%ecx")))

        elif isinstance(flatExpr, Discard):
            x86_stmts.append(NOOP(flatExpr))

        elif isinstance(flatExpr, If):
            then = []
            else_ = []
            for inst in flatExpr.then.nodes:
                then = then + translate_to_x86([inst])
            for inst in flatExpr.else_.nodes:
                else_ = else_ + translate_to_x86([inst])

            x86_stmts.append(If(flatExpr.tests, then, else_))

        elif isinstance(flatExpr, While):
            body = []
            for inst in flatExpr.body.nodes:
                body = body + translate_to_x86([inst])
            x86_stmts.append(While(flatExpr.tests, body))

        elif isinstance(flatExpr, Assign):
            expr = flatExpr.expr
            if isinstance(expr, CallFunc):
                    for a in expr.args:
                        x86_stmts.append(Push(a))
                    x86_stmts.append(Call(expr))
                    x86_stmts.append(Movl(Name("%eax"), Name(flatExpr.nodes[0].name)))
                    x86_stmts.append(Addl(Const(4*len(expr.args)), Name("%esp")))

            elif isinstance(expr, Add):
                if isinstance(flatExpr.nodes[0], Name) and expr.right.name == flatExpr.nodes[0].name:
                    x86_stmts.append(Addl(expr.left, Name(flatExpr.nodes[0].name)))
                else:
                    x86_stmts.append(Movl(expr.left, Name(flatExpr.nodes[0].name)))
                    x86_stmts.append(Addl(expr.right, Name(flatExpr.nodes[0].name)))

            elif isinstance(expr, Sub):
                if isinstance(flatExpr.nodes[0], Name) and expr.right.name == flatExpr.nodes[0].name:
                    x86_stmts.append(Subl(expr.left, Name(flatExpr.nodes[0].name)))
                else:
                    x86_stmts.append(Movl(expr.left, Name(flatExpr.nodes[0].name)))
                    x86_stmts.append(Subl(expr.right, Name(flatExpr.nodes[0].name)))

            elif isinstance(expr, UnarySub):
                if isinstance(expr.expr, Const):
                    x86_stmts.append(Movl(expr.expr, Name(flatExpr.nodes[0].name)))
                    x86_stmts.append(Negl(Name(flatExpr.nodes[0].name)))
                else:
                    x86_stmts.append(Movl(Name(expr.expr.name), Name(flatExpr.nodes[0].name)))
                    x86_stmts.append(Negl(Name(flatExpr.nodes[0].name)))

            elif isinstance(expr, Not):
                x86_stmts.append(Movl(Name(expr.expr.name), Name(flatExpr.nodes[0].name)))
                x86_stmts.append(Notl(Name(flatExpr.nodes[0].name)))
            elif isinstance(expr, Unbox):
                x86_stmts.append(Push(expr.arg))
                x86_stmts.append(Call(Name('unbox_' + expr.typ)))
                x86_stmts.append(Movl(Name('%eax'), Name(flatExpr.nodes[0].name)))
                x86_stmts.append(Addl(Const(4), Name("%esp")))
            elif isinstance(expr, Box):
                x86_stmts.append(Push(expr.arg))
                x86_stmts.append(Call(Name('box_' + expr.typ)))
                x86_stmts.append(Movl(Name('%eax'), Name(flatExpr.nodes[0].name)))
                x86_stmts.append(Addl(Const(4), Name("%esp")))
            elif isinstance(expr, Equals):
                x86_stmts.append(Equalsx86((expr.left, expr.right),flatExpr.nodes[0].name))
            elif isinstance(expr, NotEquals):
                x86_stmts.append(NotEqualsx86((expr.left, expr.right),flatExpr.nodes[0].name))
            elif isinstance(expr, AssName):
                x86_stmts.append(Movl(Name(expr.name), Name(flatExpr.nodes[0].name)))
            elif isinstance(expr, Const):
                x86_stmts.append(Movl(expr, Name(flatExpr.nodes[0].name)))
            elif isinstance(expr, Name):
                x86_stmts.append(Movl(Name(expr.name), Name(flatExpr.nodes[0].name)))
            else:
                print
                print expr
                raise Exception('error in translate_worker: invalid assign 1')
        else:
            print
            print flatExpr
            raise Exception('error in translate_worker: invalid assign 2')
    return x86_stmts

def translate(n):
    stmt = []
    stmt.append(translate_to_x86(n))
    return stmt