class Movl:
    def __init__(self, value, dest):
        self.value = value
        self.dest = dest

    def __repr__(self):
        return "movl    " + str(self.value) + ", " + str(self.dest)

    def vars(self):
        return [self.value, self.dest]

class Addl:
    def __init__(self, value, dest):
        self.value = value
        self.dest = dest

    def __repr__(self):
        return "addl    " + str(self.value) + ", " + str(self.dest)

    def vars(self):
        return [self.value, self.dest]


class Subl:
    def __init__(self, value, dest):
        self.value = value
        self.dest = dest

    def __repr__(self):
        return "subl    " + str(self.value) + ", " + str(self.dest)

    def vars(self):
        return [self.value, self.dest]


class Var:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "Var(" + str(self.value) + ")"


class Int:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "Int(" + str(self.value) + ")"


class Call:
    def __init__(self, name):
        self.funcName = name

    def __repr__(self):
        return "calll   " + str(self.funcName)

    def vars(self):
        return []


class Xorl:
    def __init__(self, value, dest):
        self.value = value
        self.dest = dest

    def __repr__(self):
        return "xorl    " + str(self.value) + ", " + str(self.dest)

class Push:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "pushl   " + str(self.value)


class Pop:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "popl    " + str(self.value)


class Reg:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "Reg(" + str(self.value) + ")"


class PrintX86:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "PrintX86(%s)" % (repr(self.value))


class NOOP:
    def __init__(self, node):
        self.node = node

    def __repr__(self):
        return "noop    " + str(self.node)


class Negl:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "negl    " + str(self.name)

class Notl:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "notl    " + str(self.name)

class Equalsx86:
    def __init__(self, operands, name):
        self.left = operands[0]
        self.right = operands[1]
        self.name = name

    def __repr__(self):
        return "x86Equals(%s, %s, %s)" % (repr(self.left), repr(self.right), repr(self.name))

class NotEqualsx86:
    def __init__(self, operands, name):
        self.left = operands[0]
        self.right = operands[1]
        self.name = name

    def __repr__(self):
        return "x86NotEquals(%s, %s, %s)" % (repr(self.left), repr(self.right), repr(self.name))

class Cmpl:

    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def __repr__(self):
        return "Cmpl(%s, %s)" % (repr(self.op1), repr(self.op2))


class JmpEqual:

    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return "JmpEqual(%s)" % (repr(self.label))


class JmpTo:

    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return "JmpTo(%s)" % (repr(self.label))


class Label:

    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return "JmpTo(%s)" % (repr(self.label))

