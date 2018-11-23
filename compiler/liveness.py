from AST import *
from assembly import *

RESERVE = set(['%esp', '%ebp', '%eax', '%edx'])

def liveness_analysis(n, l_after):
    live_variables = [l_after]
    instructions = []
    n.reverse()
    for node in n:
        if isinstance(node, Push):
            read = set()
            if isinstance(node.value, Name) and node.value.name not in RESERVE:
                read.add(node.value.name)
            live_variables.append(live_variables[-1] | read)
            instructions.append(node)
        elif isinstance(node, Pop):
            write = set()
            if isinstance(node.value, Name) and node.value.name not in RESERVE:
                write.add(node.value.name)
            live_variables.append(live_variables[-1])
            instructions.append(node)
        elif isinstance(node, PrintX86):
            read = set()
            if isinstance(node.value, Name) and node.value.name not in RESERVE:
                read.add(node.value.name)
            live_variables.append(live_variables[-1] | read)
            instructions.append(node)
        elif isinstance(node, Movl):
            read = set()
            if isinstance(node.value, Name) \
                    and node.value.name not in RESERVE \
                    and node.value.name[:12] != "unspillable$":
                read.add(node.value.name)
            write = set()
            if isinstance(node.dest, Name) \
                    and node.dest.name not in RESERVE \
                    and node.dest.name[:12] != "unspillable$":
                write.add(node.dest.name)
            l_before = (live_variables[-1] - write) | read
            live_variables.append(l_before)
            instructions.append(node)
        elif isinstance(node, Addl) or isinstance(node, Subl):
            read = set()
            write = set()
            if isinstance(node.value, Name) \
                    and node.value.name not in RESERVE \
                    and node.value.name[:12] != "unspillable$":
                read.add(node.value.name)
            #create write set
            if isinstance(node.dest, Name) \
                    and node.dest.name not in RESERVE \
                    and node.dest.name[:12] != "unspillable$":
                write.add(node.dest.name)
            l_before = (live_variables[-1] - write) | read
            live_variables.append(l_before)
            instructions.append(node)
        elif isinstance(node, Call):
            read = set()
            # if isinstance(node.funcName, Name):
                # read.add(node.funcName.name)
            instructions.append(node)
            live_variables.append(live_variables[-1] | read)
        elif isinstance(node, Negl) or isinstance(node, Notl):
            if isinstance(node.name, Name) and node.name.name not in RESERVE:
                live_variables.append(live_variables[-1] | set([node.name.name]))
            else:
                live_variables.append(live_variables[-1])
            instructions.append(node)
        elif isinstance(node, NOOP):
            live_variables.append(live_variables[-1])
            instructions.append(node)
        elif isinstance(node, If):
            then_live = liveness_analysis(node.then, live_variables[-1])
            else_live = liveness_analysis(node.else_, live_variables[-1])
            live = set([])
            for l in zip(*then_live)[1]:
                for e in l:
                    live.add(e)
            for l in zip(*else_live)[1]:
                for e in l:
                    live.add(e)
            live.add(node.tests.name)
            live_variables.append(live)
            instructions.append(node)
        elif isinstance(node, While):
            l4 = live_variables[-1]
            l2 = set([])
            cond = set([node.tests.name])
            while True:
                old_l2 = l2
                l1 = l4 | l2 | cond
                l0 = l1
                l3 = l1
                l2 = set([])
                l2_live = liveness_analysis(node.body, l3)
                for l in zip(*l2_live)[1]:
                    for e in l:
                        l2.add(e)
                if ((l0 == l1 == l3) and (old_l2 == l2)):
                    live_variables.append(l0)
                    break


            instructions.append(node)
            live_variables.append(set([node.tests.name]))



        elif isinstance(node, Equalsx86) or isinstance(node, NotEqualsx86):
            read = set()
            if isinstance(node.left, Name) \
                    and node.left.name not in RESERVE \
                    and node.left.name[:12] != "unspillable$":
                read.add(node.left.name)
            if isinstance(node.right, Name) \
                    and node.right.name not in RESERVE \
                    and node.right.name[:12] != "unspillable$":
                read.add(node.right.name)
            l_before = live_variables[-1] | read
            live_variables.append(l_before)
            instructions.append(node)

        else:
            print
            print node
            raise Exception('Error in liveness analysis: unrecognized x86 AST node')
    result = zip(instructions, live_variables)
    result.reverse()
    n.reverse()
    return result