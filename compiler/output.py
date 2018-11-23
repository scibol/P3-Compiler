
from spill import *

TEMP_COUNT = 0
ATOMIC     = 0
BINDINGS   = 1

def getPrologue(func_name, numVars):
    space = "		"
    prologueStatement = [".section	__TEXT,__text,regular,pure_instructions\n \
                    .macosx_version_min 10, 13\n \
                    .globl	_main\n \
                    .p2align	4, 0x90\n \
                    _main:                                  ## @main\n \
                    ## BB#0:\n \
                            pushl %ebp", space + "movl %esp, %ebp"]
    if (numVars > 0):
        prologueStatement.append(space + "subl " + "$" + str(numVars*4) + ", %esp")
    return prologueStatement

# Write the epilogue of the program
# return: the a list of assembly instructions corresponding to the epilogue
def getEpilogue(func_name):
    space = "		"
    if func_name == "main":
        return [space + "movl $0, %eax", space + "leave", space + "ret"]
    return [space + "popl %edi",space + "popl %esi", space + "popl %ebx", space + "leave", space + "ret"]

# Write the body of the program
# x86Stmts: a list of x86 AST nodes
#return: a list of assembly instructions corresponding to the body

def getBody(x86Stmts, mapping):
    space = "		"
    code = []
    for stmt in x86Stmts:
        if isinstance(stmt, Push):
            if isinstance(stmt.value, Const):
                code.append(space + "pushl " + "$" + str(stmt.value.value))
            elif isinstance(stmt.value, Name):
                if "func$" in stmt.value.name:
                    code.append(space + "pushl " + stmt.value.name)
                else:
                    code.append(space + "pushl " + mapping[stmt.value.name])
            else:
                if stmt.value:
                    code.append(space + "pushl " + mapping[stmt.value])
        elif isinstance(stmt, Pop):
            code.append(space + "popl " + mapping[stmt.value.name])
        elif isinstance(stmt, Movl):
            if isinstance(stmt.value, Const):
                code.append(space + "movl " + "$" + str(stmt.value.value) + ", " + mapping[stmt.dest])
            else:
                if ('-' in mapping[stmt.value.name]) and ('-' in mapping[stmt.dest.name]):
                    code.append(space + "pushl %ebx")
                    code.append(space + "movl " + mapping[stmt.value.name] + ", %ebx")
                    code.append(space + "movl %ebx, " + mapping[stmt.dest.name])
                    code.append(space + "popl %ebx")
                else:
                    code.append(space + "movl " + mapping[stmt.value.name] + ", " + mapping[stmt.dest.name])
        elif isinstance(stmt, Addl):
            if isinstance(stmt.value, Const):
                code.append(space + "addl " + "$" + str(stmt.value.value) + ", " + mapping[stmt.dest.name])
            else:
                if (('-' in mapping[stmt.value.name]) and ('-' in mapping[stmt.dest.name])):
                    code.append(space + "pushl %ebx")
                    code.append(space + "movl " + mapping[stmt.value.name] + ", %ebx")
                    code.append(space + "addl %ebx, " +  mapping[stmt.dest.name])
                    code.append(space + "popl %ebx")
                else:
                    code.append(space + "addl " + mapping[stmt.value.name] + ", " + mapping[stmt.dest.name])
        elif isinstance(stmt, Call):
            if isinstance(stmt.funcName, Name):
                if "$" in stmt.funcName.name and "func" not in stmt.funcName.name:
                    code.append(space + "call *" + mapping[stmt.funcName.name])
                else:
                    code.append(space + "call " + stmt.funcName.name)
            if isinstance(stmt.funcName, CallFunc):
                code.append(space + "call " + stmt.funcName.node.name)
        elif isinstance(stmt, PrintX86):
            code.append(space + "call print_int_nl")
        elif isinstance(stmt, Negl):
            code.append(space + "negl " + mapping[stmt.name.name])
        # elif isinstance(stmt, And):
        #     code.append(space + "andl " + mapping[stmt.op1.name]+ ", " + mapping[stmt.op2.name])
        # elif isinstance(stmt, Or):
        #     code.append(space + "orl " + mapping[stmt.op1.name]+ ", " + mapping[stmt.op2.name])
        # elif isinstance(stmt, Notl):
        #     code.append(space + "notl " + mapping[stmt.expr.name])
        elif isinstance(stmt, NOOP):
            code.append(space + "NOP")
        elif isinstance(stmt, Cmpl):
            if isinstance(stmt.op1, Const):
                code.append(space + "cmpl " + "$" + str(stmt.op1.value) + ", " + mapping[stmt.op2.name])
            else:
                code.append(space + "cmpl " + mapping[stmt.op1.name] + ", " + mapping[stmt.op2.name])
        elif isinstance(stmt, JmpEqual):
            code.append(space + "je " + stmt.label)
        elif isinstance(stmt, JmpTo):
            code.append(space + "jmp " + stmt.label)
        elif isinstance(stmt, Label):
            code.append(stmt.label)
        else:
            print
            print
            print stmt
            raise Exception('Error in prettyPrint: no class')
    return code

# x86Stmts: a list of flattened x86 nodes
# numVars: the total number of vaiables in the list of instructions
# return: a list 'pretty' assembly code

def prettyPrint(x86Stmts, numVars, mapping):
    prologue = getPrologue('main', numVars)
    codeBody = getBody(x86Stmts, mapping)
    epilogue = getEpilogue('main')
    return prologue + codeBody + epilogue