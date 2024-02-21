from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def isCyclicUtil(self, v, visited, parent, cycle_nodes):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                if self.isCyclicUtil(i, visited, v, cycle_nodes):
                    return True
            elif parent != i:
                if i not in cycle_nodes:
                    cycle_nodes.append(i)
                if v not in cycle_nodes:
                    cycle_nodes.append(v)
                return True
        return False

    def isCyclic(self):
        visited = [False] * (self.V)
        for i in range(self.V):
            if visited[i] == False:
                cycle_nodes = []
                if self.isCyclicUtil(i, visited, -1, cycle_nodes) == True:
                    print("Cycle found with nodes:", cycle_nodes)
                    return True
        return False

g = Graph(5)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)

if g.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph doesn't contain cycle")

g1 = Graph(3)
g1.addEdge(0, 1)
g1.addEdge(1, 2)

if g1.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph doesn't contain cycle")
