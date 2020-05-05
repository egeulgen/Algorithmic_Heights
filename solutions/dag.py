import sys


class directed_graph:
    def __init__(self):
        self.nodes = {}

    class node:
        def __init__(self, label):
            self.label = label
            self.target_nodes = []
            self.visited = False

    def add_node(self, label):
        node = self.node(label)
        self.nodes[label] = node

    def remove_node(self, label):
        del self.nodes[label]
        for node in self.nodes.values():
            for i, target in enumerate(node.target_nodes):
                if target.label == label:
                    del node.target_nodes[i]

    def construct_graph(self, n, edge_list):
        for i in range(1, n + 1):
            self.add_node(i)

        for edge in edge_list:
            self.nodes[edge[0]].target_nodes.append(self.nodes[edge[1]])

    def is_acyclic(self):
        if len(self.nodes) == 0:
            return 1

        if not any(len(v.target_nodes) == 0 for v in self.nodes.values()):
            return -1

        for node in self.nodes.values():
            if len(node.target_nodes) == 0:
                self.remove_node(node.label)
                return self.is_acyclic()


if __name__ == "__main__":
    '''
    Given: A positive integer k≤20 and k simple directed graphs in the edge list format with at most 103 vertices and 
    3⋅103 edges each.
    Return: For each graph, output "1" if the graph is acyclic and "-1" otherwise.
    '''
    input_lines = sys.stdin.read().splitlines()
    k = int(input_lines[0])

    i = 2
    n_vert_list = []
    edge_lists = []
    while i < len(input_lines):
        num_vertices, num_edges = [int(x) for x in input_lines[i].split()]
        n_vert_list.append(num_vertices)
        edge_lists.append([[int(x) for x in line.split()] for line in input_lines[i + 1: i + 1 + num_edges]])
        i = i + 1 + num_edges + 1

    result = []
    for num_vertices, edge_list in zip(n_vert_list, edge_lists):
        G = directed_graph()
        G.construct_graph(num_vertices, edge_list)
        result.append(str(G.is_acyclic()))
    print(" ".join(result))