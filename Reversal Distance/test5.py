seq = [0,3,1,5,2,6,4,7]

def bp_pair(ident_list: list) -> dict:
    break_point = []
   
    for i in range(len(ident_list)-1):
        if abs(ident_list[i] - ident_list[i + 1]) != 1:
            break_point.append((ident_list[i],ident_list[i+1]))

    return break_point
breakpoints = bp_pair(seq)

def find_num_bp(break_points):
    print(break_points)
    dic_bp = {}
    for bp in break_points:

        for point in bp:
            
            if point not in dic_bp:
                dic_bp[point] = [bp]
                print(point,bp)
            else:
                dic_bp[point].append(bp)
    nodes = {}
    for bp_key in dic_bp:
        for bp in dic_bp[bp_key]:
            values = []
            if (bp_key - 1) in dic_bp:
                for bp1 in dic_bp[bp_key - 1]:
                    values.append((bp_key - 1,bp1))
            if (bp_key + 1) in dic_bp:
                for bp2 in dic_bp[bp_key + 1]:
                    values.append((bp_key + 1, bp2))
            nodes[(bp_key,bp)] = values
    return nodes


def find_cycle(graph, start_node, current_node, visited_seq, visited):
    # DFS to find a cycle in the graph
    visited.add(current_node)
    
    for neighbor in graph[current_node]:
        point_1 = neighbor[1][0]
        point_2 = neighbor[1][1]
        if neighbor == start_node:
            # Found a cycle
            return [current_node, neighbor]
        elif neighbor not in visited  and not point_1 and not point_2:
            # Recursively search for a cycle starting from the neighbor
            cycle = find_cycle(graph, start_node, neighbor, visited.copy())
            if cycle:
                return [current_node] + cycle
    
    return None


def find_cycles(seq,graph):
    # Function to find all cycles in the graph
    cycles = []
    visited_seq = [False]*len(seq)
    for node in graph.keys():
        for point in node[1]:
            visited_seq[point] = True
        for neighbor in graph[node]:
            point_1 = neighbor[1][0]
            point_2 = neighbor[1][1]
            if neighbor in graph[node] and not point_1 and not point_2: # this part is very questionable
                cycle = find_cycle(graph, node, neighbor, visited_seq, set())
                if cycle:
                    cycle = [node] + cycle
                    cycles.append(cycle)
    return cycles




# Find cycles in the graph
breakpoints = bp_pair(seq)
breakpoint_helper = find_num_bp(breakpoints)
print(breakpoint_helper)

cycles = find_cycles(seq, breakpoint_helper)
print("Cycles:", cycles)
