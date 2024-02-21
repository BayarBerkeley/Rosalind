from collections import defaultdict

class Graph:
    def __init__(self):
        # Initialize the graph with a defaultdict where the values are lists
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Add an edge from vertex u to vertex v in the graph
        self.graph[u].append(v)

    def shortest_cycle_util(self, v, visited, path):
        # Utility function to find the shortest cycle starting from vertex v
        visited[v] = True  # Mark the current vertex as visited
        path.append(v)  # Add the current vertex to the path

        # Traverse through all the neighbors of the current vertex
        for neighbor in self.graph[v]:
            # If the neighbor is the starting node and the path has more than 2 nodes (complete cycle found)
            if neighbor == path[0] and len(path) > 2:
                path.append(neighbor)  # Add the starting node to complete the cycle
                return path

            # If the neighbor has not been visited yet, recursively search for a cycle
            if not visited[neighbor]:
                cycle = self.shortest_cycle_util(neighbor, visited, path)
                if cycle:
                    return cycle

        path.pop()  # Remove the current vertex from the path as it leads to no cycle
        return None

    def shortest_cycle(self):
        shortest_cycle = None  # Initialize the shortest cycle to None
        min_cycle_length = float('inf')  # Initialize the minimum cycle length to positive infinity

        # Iterate through all vertices in the graph
        for node in range(len(self.graph)):
            visited = [False] * len(self.graph)  # Initialize visited list for each vertex
            path = []  # Initialize an empty path
            cycle = self.shortest_cycle_util(node, visited, path)  # Find shortest cycle starting from current vertex
            # If a cycle is found and its length is smaller than the current minimum cycle length
            if cycle and len(cycle) < min_cycle_length:
                shortest_cycle = cycle  # Update the shortest cycle
                min_cycle_length = len(cycle)  # Update the minimum cycle length

        return shortest_cycle  # Return the shortest cycle, if found

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 2)

shortest_cycle = g.shortest_cycle()
if shortest_cycle:
    print("Shortest cycle in the graph:", shortest_cycle)
else:
    print("No cycle found in the graph")
