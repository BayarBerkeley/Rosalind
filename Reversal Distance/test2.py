class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, u, v):
        if u in self.graph and v in self.graph:
            self.graph[u].append(v)
            # Uncomment the following line if the graph is undirected
            # self.graph[v].append(u)
        else:
            print("Vertices not found in the graph.")

    def display(self):
        print("Graph:")
        for vertex, edges in self.graph.items():
            print(vertex, "->", edges)


# Example usage:
g = Graph()

# Adding vertices
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)

# Adding edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# Displaying the graph
g.display()
