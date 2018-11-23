from AST import *
from assembly import *

INSTRUCTIONS = 0
LIVE_VARS    = 1

def get_variables(instructions):
    interference_graph = {"%eax" : set(), "%ebx" : set(), "%ecx" : set(), "%edx" : set(), "%esi" : set(), "%edi": set()}
    for instruction in instructions:
        if isinstance(instruction, Movl):
            if isinstance(instruction.value, Name):
                interference_graph[instruction.value.name] = set()
            if isinstance(instruction.dest, Name):
                interference_graph[instruction.dest.name] = set()
        elif isinstance(instruction, If):
            then = get_variables(instruction.then)
            for var in then.keys():
                interference_graph[var] = set()
            else_ = get_variables(instruction.else_)
            for var in else_.keys():
                interference_graph[var] = set()
            interference_graph[instruction.tests.name] = set()
        elif isinstance(instruction, Addl) or isinstance(instructions, Subl):
            if isinstance(instruction.value, Name):
                interference_graph[instruction.value.name] = set()
            if isinstance(instruction.dest, Name):
                interference_graph[instruction.dest.name] = set()
        elif isinstance(instruction, Negl) or isinstance(instructions, Notl):
            if isinstance(instruction.name, Name):
                interference_graph[instruction.name.name] = set()
        elif isinstance(instruction, Pop):
            if isinstance(instruction.value, Name):
                interference_graph[instruction.value.name] = set()
        elif isinstance(instruction, Push):
            if isinstance(instruction.value, Name):
                interference_graph[instruction.value.name] = set()
        elif isinstance(instruction, Equalsx86) or isinstance(instructions, NotEqualsx86):
            if isinstance(instruction.left.name, Name):
                interference_graph[instruction.left.name.name] = set()
            if isinstance(instruction.right.name, Name):
                interference_graph[instruction.right.name.name] = set()
        elif isinstance(instruction, While):
            body = get_variables(instruction.body)
            for var in body:
                interference_graph[var] = set()
                test = get_variables([instruction.tests])
            for var in test:
                interference_graph[var] = set()
            if isinstance(instruction.tests, Name):
                interference_graph[instruction.tests.name] = set()
    if "%esp" in interference_graph.keys():
        del interference_graph["%esp"]
    if "%ebp" in interference_graph.keys():
        del interference_graph["%ebp"]
    return interference_graph

def remove_ints(graph):
    for key in graph.keys():
        if isinstance(key, int):
            del graph[key]
        else:
            graph[key] = set([e for e in graph[key] if not isinstance(e, int)])
    return graph

def generate_rig(inst_live_pair):
    interference_graph = get_variables([list(e) for e in zip(*inst_live_pair)][INSTRUCTIONS])

    for pair in inst_live_pair:
        instruction = pair[INSTRUCTIONS]
        live_vars = pair[LIVE_VARS]
        if isinstance(instruction, Movl) or isinstance(instruction, Addl) or isinstance(instruction, Subl):
            right_name = instruction.dest.name
            left_name  = ''
            if isinstance(instruction.value, Name):
                left_name = instruction.value.name
            for var in live_vars:
                if right_name not in ["%esp", "%ebp"]:
                    interference_graph[right_name].add(var)
                    interference_graph[var].add(right_name)
            if left_name is not '':
                for var in live_vars:
                    if right_name not in ["%esp", "%ebp"]:
                        interference_graph[left_name].add(var)
                        interference_graph[var].add(left_name)
            for var1 in live_vars:
                for var2 in live_vars:
                    if var1 != var2:
                        interference_graph[var1].add(var2)
                        interference_graph[var2].add(var1)
        elif isinstance(instruction, If) or isinstance(instruction, While):
            for var1 in live_vars:
                for var2 in live_vars:
                    if var1 != var2:
                        interference_graph[var1].add(var2)
                        interference_graph[var2].add(var1)
        elif isinstance(instruction, Call) or isinstance(instruction, PrintX86):
            for var in live_vars:
                interference_graph[var] = interference_graph[var] | set(["%eax", "%edx", "%ecx"])
                interference_graph["%eax"].add(var)
                interference_graph["%edx"].add(var)
                interference_graph["%ecx"].add(var)
        elif isinstance(instruction, Negl) or isinstance(instruction, Notl):
            name = ""
            if isinstance(instruction.name, Name):
                name = instruction.name.name

                for var in live_vars:
                    if var != name:
                        interference_graph[name].add(var)
                        interference_graph[var].add(name)
    return remove_ints(interference_graph)