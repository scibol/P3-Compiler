from AST import *


def expl(ast):
    if isinstance(ast, Module):
        return Module(ast.doc, expl(ast.node))

    elif isinstance(ast, Stmt):
        fnodes = map(expl, ast.nodes)
        return Stmt(fnodes)

    elif isinstance(ast, Printnl):
        e = expl(ast.nodes[0])
        return Printnl([e], ast.dest)

    elif isinstance(ast, Const):
        if ast.value == "True":
            ast.value = 1
            return Box("bool", ast)
        elif ast.value == "False":
            ast.value = 0
            return Box("bool", ast)
        else:
            return Box("int", ast)

    elif isinstance(ast, Assign):
        r = expl(ast.expr)
        l = ast.nodes[0]
        if isinstance(l, AssName):
            return Assign(nodes=ast.nodes, expr=r)

    elif isinstance(ast, Name):
        return ast

    elif isinstance(ast, Add):
        lExpr = expl(ast.left)
        rExpr = expl(ast.right)

        return Box("int", Add((Unbox("int", lExpr), Unbox("int", rExpr))))

    elif isinstance(ast, Sub):
        lExpr = expl(ast.left)
        rExpr = expl(ast.right)

        return Box("int", Sub((Unbox("int", lExpr), Unbox("int", rExpr))))

    elif isinstance(ast, And):
        lExpr = expl(ast.left)
        rExpr = expl(ast.right)
        return Box("bool", CallFunc("and_", (lExpr, rExpr), None, None))

    elif isinstance(ast, Or):
        lExpr = expl(ast.left)
        rExpr = expl(ast.right)
        return Box("bool", CallFunc("or_", (lExpr, rExpr), None, None))

    elif isinstance(ast, While):
        test = expl(ast.tests)
        body = expl(ast.body)
        return While(Unbox("bool", test), body)

    elif isinstance(ast, If):
        tests = expl(ast.tests)
        then = expl(ast.then)
        else_ = expl(ast.else_)
        return If(Unbox("bool", tests), then, else_)

    elif isinstance(ast, Not):
        expr = expl(ast.expr)
        return Box("bool", Not(Unbox("bool", expr)))

    elif isinstance(ast, CallFunc):
        node = expl(ast.node)
        args = map(expl, ast.args)
        return Box("int", CallFunc(node, args, None, None))

    elif isinstance(ast, UnarySub):
        expr = expl(ast.expr)
        return Box("int", UnarySub(Unbox("int", expr)))

    elif isinstance(ast, UnaryAdd):
        expr = expl(ast.expr)
        return Box("int", UnaryAdd(Unbox("int", expr)))

    elif isinstance(ast, Equals):
        left = expl(ast.left)
        right = expl(ast.right)
        return Box("bool", Equals((Unbox("bool", left), Unbox("bool", right))))

    elif isinstance(ast, NotEquals):
        left = expl(ast.left)
        right = expl(ast.right)
        return Box("bool", NotEquals((Unbox("bool", left), Unbox("bool", right))))

    elif isinstance(ast, Discard):
        expr1 = expl(ast.expr)
        return Discard(expr1)

    else:
        print "ERRORONE!!!"
        print ast
