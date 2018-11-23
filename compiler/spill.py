from AST import *
from assembly import *

TEMP_COUNT = 0

def get_spill_var_name():
    global TEMP_COUNT
    variable_name = "unspillable$" + str(TEMP_COUNT)
    TEMP_COUNT = TEMP_COUNT + 1
    return variable_name


def generate_spill_code(instructions, spilled, spill_num):
    generated_code = []
    spill_count = 0
    global TEMP_COUNT
    TEMP_COUNT = spill_num
    for instruction in instructions:
        if isinstance(instruction, Movl) \
                and isinstance(instruction.value, Name) \
                and (instruction.dest.name in spilled.keys()) \
                and (instruction.value.name in spilled.keys()):
            spill_var = get_spill_var_name()
            generated_code.append(Movl(instruction.value, Name(spill_var)))
            generated_code.append(Movl(Name(spill_var), instruction.dest))
            spill_count = spill_count + 1
        elif isinstance(instruction, If):
            then, then_spill_count = generate_spill_code(instruction.then, spilled, spill_count)
            else_, else_spill_count = generate_spill_code(instruction.else_, spilled, spill_count+then_spill_count)
            spill_count = spill_count + then_spill_count + else_spill_count
            generated_code.append(If(instruction.tests,then, else_))
        elif isinstance(instruction, Addl) \
                and isinstance(instruction.value, Name) \
                and (instruction.dest.name in spilled.keys()) \
                and (instruction.value.name in spilled.keys()):
            spill_var = get_spill_var_name()
            generated_code.append(Movl(instruction.value, Name(spill_var)))
            generated_code.append(Addl(Name(spill_var), instruction.dest))
            spill_count = spill_count + 1
        elif isinstance(instruction, Subl) \
                and isinstance(instruction.value, Name) \
                and (instruction.dest.name in spilled.keys()) \
                and (instruction.value.name in spilled.keys()):
            spill_var = get_spill_var_name()
            generated_code.append(Movl(instruction.value, Name(spill_var)))
            generated_code.append(Subl(Name(spill_var), instruction.dest))
            spill_count = spill_count + 1
        else:
            generated_code.append(instruction)
    return (generated_code, spill_count)