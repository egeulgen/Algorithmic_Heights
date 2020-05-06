import sys


class directed_graph:
    def __init__(self):
        self.nodes = {}
        self.clock = 0

    class node:
        def __init__(self, label):
            self.label = label
            self.target_nodes = []
            self.visited = False
            self.post = 0

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

    def explore(self, node):
        node.visited = True
        for target_node in node.target_nodes:
            if not target_node.visited:
                self.explore(target_node)
        node.post = int(self.clock)
        self.clock += 1

    def DFS(self):
        for node in self.nodes.values():
            if not node.visited:
                self.explore(node)

    def topological_sorting(self):
        self.DFS()
        all_node_labels = list(self.nodes.keys())
        sorting = []

        while all_node_labels:
            max_label = max((label for label in all_node_labels), key=lambda x: self.nodes[x].post)
            all_node_labels.remove(max_label)
            sorting.append(max_label)
        return sorting


if __name__ == "__main__":
    '''
    Given: A simple directed acyclic graph with n≤103 vertices in the edge list format.
    Return: A topological sorting (i.e., a permutation of vertices) of the graph.
    '''
    input_lines = sys.stdin.read().splitlines()
    num_vertices, num_edges = [int(x) for x in input_lines[0].split()]
    edge_list = [[int(x) for x in line.split()] for line in input_lines[1: ]]

    G = directed_graph()
    G.construct_graph(num_vertices, edge_list)
    result = G.topological_sorting()
    print(" ".join(map(str, result)))