class Node:

    def __init__(self):
        pass


class Module():

    def __init__(self, doc, node):
        self.doc = doc
        self.node = node

    def __str__(self):
        return self.__class__.__name__ + "(" + str(self.doc) + ", " + str(self.node) + ")"

    def __repr__(self):
        return self.__str__()


class Stmt:

    def __init__(self, nodes):
        self.nodes = nodes

    def __str__(self):
        return self.__class__.__name__ + "(" + str(self.nodes) + ")"

    def __repr__(self):
        return self.__str__()


class Add:

    def __init__(self, operands):
        self.left = operands[0]
        self.right = operands[1]

    def __str__(self):
        return self.__class__.__name__ + "((" + str(self.left) + ", " + str(self.right) + "))"

    def __repr__(self):
        return self.__str__()


class UnaryAdd:

    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        return self.__class__.__name__ + "(" + str(self.expr) + ")"

    def __repr__(self):
        return self.__str__()


class UnarySub:

    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        return self.__class__.__name__ + "(" + str(self.expr) + ")"

    def __repr__(self):
        return self.__str__()

class Sub:

    def __init__(self, operands):
        self.left = operands[0]
        self.right = operands[1]

    def __str__(self):
        return self.__class__.__name__ + "((" + str(self.left) + ", " + str(self.right) + "))"

    def __repr__(self):
        return self.__str__()

class Const:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.__class__.__name__ + "(" + str(self.value) + ")"

    def __repr__(self):
        return self.__str__()

class Printnl:

    def __init__(self, nodes, dest):
        self.nodes = nodes
        self.dest = dest

    def __str__(self):
        return self.__class__.__name__ + "(" + str(self.nodes) + ", " + str(self.dest) + ")"

    def __repr__(self):
        return self.__str__()

class AssName:

    def __init__(self, name, flags):
        self.name = name
        self.flags = flags

    def __str__(self):
        return self.__class__.__name__ + "('" + str(self.name) + "', '" + str(self.flags) + "')"

    def __repr__(self):
        return self.__str__()

class Assign:

    def __init__(self, nodes, expr):
        self.nodes = nodes
        self.expr = expr

    def __str__(self):
        return self.__class__.__name__ + "(" + str(self.nodes) + ", " + str(self.expr) + ")"

    def __repr__(self):
        return self.__str__()

class Name:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.__class__.__name__ + "('" + str(self.name) + "')"

    def __repr__(self):
        return self.__str__()

class Discard:

    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        return self.__class__.__name__ + "(" + str(self.expr) + ")"

    def __repr__(self):
        return self.__str__()


class CallFunc:

    def __init__(self, node, args, star_args, dstar_args):
        self.node = node
        self.args = args
        self.star_args = star_args
        self.dstar_args = dstar_args

    def __str__(self):
        return "CallFunc(%s, %s, %s, %s)" % (self.node, repr(self.args), self.star_args, self.dstar_args)

    def __repr__(self):
        return self.__str__()


class If:
    def __init__(self, tests, then, else_ ):
        self.tests = tests
        self.then = then
        self.else_ = else_

    def __str__(self):
        return self.__class__.__name__ + "((" + str(self.tests) + "), (" + str(self.then) + "), (" + str(self.else_) + ")"

    def __repr__(self):
        return self.__str__()


class While:
    def __init__(self, tests, body ):
        self.tests = tests
        self.body = body

    def __str__(self):
        return self.__class__.__name__ + "(" + str(self.tests) + "), " + str(self.body)

    def __repr__(self):
        return self.__str__()


class Equals:

    def __init__(self, operands):
        self.left = operands[0]
        self.right = operands[1]

    def __str__(self):
        return self.__class__.__name__ + "((" + str(self.left) + ", " + str(self.right) + "))"

    def __repr__(self):
        return self.__str__()


class NotEquals:

    def __init__(self, operands):
        self.left = operands[0]
        self.right = operands[1]

    def __str__(self):
        return self.__class__.__name__ + "((" + str(self.left) + ", " + str(self.right) + "))"

    def __repr__(self):
        return self.__str__()

class And:

    def __init__(self, operands):
        self.left = operands[0]
        self.right = operands[1]

    def __str__(self):
        return self.__class__.__name__ + "((" + str(self.left) + ", " + str(self.right) + "))"

    def __repr__(self):
        return self.__str__()


class Or:

    def __init__(self, operands):
        self.left = operands[0]
        self.right = operands[1]

    def __str__(self):
        return self.__class__.__name__ + "((" + str(self.left) + ", " + str(self.right) + "))"

    def __repr__(self):
        return self.__str__()

class Not:

    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        return self.__class__.__name__ + "(" + str(self.expr) + ")"

    def __repr__(self):
        return self.__str__()



class GetTag:

    def __init__(self, typ, arg):
        self.typ = typ
        self.arg = arg

    def get_children(self):
        return [self.arg]

    def get_child_nodes(self):
        return [self.arg]

    def __repr__(self):
        return "GetTag(%s, %s)" % (self.typ, repr(self.arg))


class InjectFrom:

    def __init__(self, typ, arg):
        self.typ = typ
        self.arg = arg

    def get_children(self):
        return [self.arg]

    def get_child_nodes(self):
        return [self.arg]

    def __repr__(self):
        return "InjectFrom(%s, %s)" % (self.typ, repr(self.arg))


class ProjectTo:

    def __init__(self, typ, arg):
        self.typ = typ
        self.arg = arg

    def get_children(self):
        return [self.arg]

    def get_child_nodes(self):
        return [self.arg]

    def __repr__(self):
        return "ProjectTo(%s, %s)" % (self.typ, repr(self.arg))


class Let:
    def __init__(self, var, rhs, body):
        self.var = var
        self.rhs = rhs
        self.body = body

    def get_children(self):
        return self.rhs, self.body

    def get_child_nodes(self):
        return self.rhs, self.body

    def __repr__(self):
        return "Let(%s, %s, %s)" % \
               (self.var, repr(self.rhs), repr(self.body))

class Box:

    def __init__(self, typ, arg):
        self.typ = typ
        self.arg = arg

    def get_children(self):
        return [self.arg]

    def get_child_nodes(self):
        return [self.arg]

    def __repr__(self):
        return "Box(%s, %s)" % (self.typ, repr(self.arg))

class Unbox:

    def __init__(self, typ, arg):
        self.typ = typ
        self.arg = arg

    def get_children(self):
        return [self.arg]

    def get_child_nodes(self):
        return [self.arg]

    def __repr__(self):
        return "UnBox(%s, %s)" % (self.typ, repr(self.arg))


builtin_functions = ['input_int', 'input', 'print_any', 'is_true', 'equal']

return_type = {
    'is_true' : 'bool',
    'equal' : 'bool',
    'input_int' : 'pyobj',
    'input' : 'int'
    }