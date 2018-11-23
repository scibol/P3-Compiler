# flatExprs: a list of flat expressions
# return: a map from variables to stack locations
def mapVar(coloring, uncolored, num_vars):
    num_vars = num_vars + 1
    for var in uncolored:
        coloring[var] = "-" + str(num_vars*4) + "(%ebp)"
        num_vars = num_vars + 1
    return coloring


def preprocessor(rig, spilled_assignment):
    coloring = {"%esp" :  "%esp", "%ebp" : "%ebp", "%eax" : "%eax", "%ebx" : "%ebx", "%ecx" : "%ecx", "%edx" : "%edx", "%esi" : "%esi", "%edi" : "%edi"}
    if spilled_assignment == None:
        return coloring
    else:
        for assignment in spilled_assignment:
            coloring[assignment] = spilled_assignment[assignment]
            del rig[assignment]
        return coloring

def color_graph(rig, spilled_assignment):
    #set of colors: use registers as colors
    colors = set(["%eax", "%ebx", "%ecx", "%edx", "%esi", "%edi"])
    #dictionary of current assignments: the six registers are preassigned
    #coloring = {"%esp" :  "%esp", "%ebp" : "%ebp", "%eax" : "%eax", "%ebx" : "%ebx", "%ecx" : "%ecx", "%edx" : "%edx", "%esi" : "%esi", "%edi" : "%edi"}
    coloring = preprocessor(rig, spilled_assignment)
    spilled = []
    spill_map = {}
    numVar = len(rig.keys())

    def saturation(node, conflicts):
        current_colors = set()
        for var in conflicts:
            if var in coloring.keys():
                current_colors.add(coloring[var])
        return (len(current_colors), current_colors)

    def get_highest_saturated(rig):
        max_sat = [0, '', None]
        for node in rig.keys():
            if node not in colors:
                node_sat, colors_used = saturation(node, rig[node])
                if node_sat > max_sat[0]:
                    max_sat = [node_sat, node, colors_used]
                elif node_sat == max_sat[0]:
                    if max_sat[1][:12] != "unspillable$":
                        max_sat = [node_sat, node, colors_used]
        return (max_sat[1], max_sat[2])

    while (len(rig.keys()) > len(colors)):
        node, colors_used = get_highest_saturated(rig)
        color = (colors - colors_used)
        if len(color) > 0:
            coloring[node] = color.pop()
        else:
            spilled.append(node)
        del rig[node]

    num_vars = 0
    if (spilled_assignment != None):
        num_vars = len(spilled_assignment)
    coloring = mapVar(coloring, spilled, num_vars)
    for spill in spilled:
        spill_map[spill] = coloring[spill]
    return (coloring, spill_map)