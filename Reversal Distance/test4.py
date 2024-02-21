graph_example = {0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2,4]}
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
        print(bp)
        for point in bp:
            
            if point not in dic_bp:
                dic_bp[point] = [bp]
                print(point,bp)
            else:
                dic_bp[point].append(bp)
    
    return dic_bp


breakpoints = bp_pair(seq)
graph_helper = find_num_bp(breakpoints)
seq_marked = [[False,False]]*len(breakpoints)
marked = [False]*len(graph_helper.keys())
print(marked)
print(find_num_bp(bp_pair(seq)))

def dfs(graph, graph_helper, v_vv, path, marked, seq_marked):
    marked[v_vv[0]] = True
    marked[next(x for x in v_vv[1] if x != v_vv[0])] = True
    seq_marked[graph.index(v_vv[1])][v_vv[1].index(v_vv[0])] = True

    path.append(v_vv[1])

    next_points = []
    if (v_vv[0] + 1) in graph_helper.keys():
        next_points.append(v_vv[0] + 1)
    if (v_vv[0] - 1) in graph_helper.keys():
        next_points.append(v_vv[0] - 1)
    
    for v in next_points:
        for vv in graph_helper[v]:
            if vv == path[0] and len(path) > 1:
                path.append(vv)
                return path
            print(vv[0],vv[1])
            if not marked[vv[0]] and not marked[vv[1]]:
                cycle = dfs(graph, graph_helper, (v,vv), path, marked, seq_marked)
                if cycle:
                    return cycle
    path.pop()
    return None

print(dfs(breakpoints,graph_helper,(3,(3,1)), [], marked, seq_marked))

[(0, 3), (3, 1), (1, 5), (5, 2), (2, 6), (6, 4), (4, 7)]
graph = { 
    (0,(0,3)):[(3,1),(1,5)],
    (3,(0,3)):[(2,6),(5,2),(6,4),(4,7)],
    ()
}

