from parser import parseFile
from flatten1 import flatten_ast
from explicate import expl
from to_x86 import *
from liveness import *
from interference import *
from coloring import *
from spill import *
from labelize import *
from output import *
import sys

# def epilogue():
#     asm = "xorl %eax, %eax \n \
#                    addl     $" + str(padding) + ", %esp\n \
#                    popl     %ebp\n \
#                    retl\n\n\n"
#     asm = asm + ".subsections_via_symbols"
#     return asm
#


def merge_dict(d1, d2):
    for k in d2.keys():
        d1[k] = d2[k]
    return d1

# parse the arguments
option = "-default"

if len(sys.argv) == 3:
    option = sys.argv[1]
    if option != "-pseudo" and option != "-liveness":
        print "Option can be -pseudo or -liveness"
        sys.exit(1)
    filename = sys.argv[2]
elif len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print "Either provide filename or option filename"
    sys.exit(1)


t = parseFile(filename)

explicate = expl(t)

flattened = flatten_ast(explicate)

all_statements = translate_to_x86(flattened.node.nodes)

live_analysis = liveness_analysis(all_statements, set([]))


if option == "-liveness":
    for live in live_analysis:
        print(live[0])
        print('#live: ' + ', '.join(live[1]))
    sys.exit(1)

if option == "-pseudo":
    for live in live_analysis:
        print(live[0])
    sys.exit(1)


rig = generate_rig(live_analysis)
mapping, spilled = color_graph(rig, None)

spill_count = 0
if len(spilled) > 0:
    all_statements, spill_count = generate_spill_code(all_statements, spilled, spill_count)

if spill_count > 0:
    pair = liveness_analysis(all_statements, set([]))
    rig = generate_rig(pair)
    mapping, new_spilled = color_graph(rig, spilled)
    spilled = merge_dict(spilled, new_spilled)
    all_statements, spill_count = generate_spill_code(all_statements, spilled, spill_count)

all_statements = remove_structured_code(all_statements)

output = prettyPrint(all_statements, len(spilled), mapping)
for line in output:
    print(line)
sys.exit(0)