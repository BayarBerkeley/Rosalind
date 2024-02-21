# this problem is just for using a graph
class Tree:
    def __init__(self) -> None:
        self.tree = {}
    def add_node(self, node):
        self.tree[node] = set()
    
    def add_edge(self, node1, node2):
        self.tree[node1].add(node2)
    
    def count_edges(self, node):
        print(self.tree[node])
        return len(self.tree[node])
    def call_nodes(self):
        return self.tree.keys()
    

with open('rosalind_tree.txt', 'r') as file:
    my_tree = Tree()
    primary_node = 0
    secondary_node = 0
    node = 0
    for line in file:
        line = line.rstrip().split(' ')

        if len(line) == 1 and not primary_node:
            primary_node = int(line[0])
            my_tree.add_node(primary_node)
        elif len(line) == 1:
            secondary_node = int(line[0])
            my_tree.add_node(secondary_node)
        elif len(line) == 2:
            node = int(line[1])
            if primary_node != node and not secondary_node:
                my_tree.add_edge(primary_node, node)
            else:
                my_tree.add_edge(secondary_node,node)
    
    count_edges = 0

    nodes = my_tree.call_nodes()
    
    print(nodes)
    for node in nodes:
        count_edges +=my_tree.count_edges(node)
    
    print(count_edges)

