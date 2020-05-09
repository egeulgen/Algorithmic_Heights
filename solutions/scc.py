import sys


class directed_graph:
    def __init__(self):
        self.nodes = {}
        self.rev_nodes = {}
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
        node = self.node(label)
        self.rev_nodes[label] = node

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
            self.rev_nodes[edge[1]].target_nodes.append(self.rev_nodes[edge[0]])

    def fill_order(self, node, stack):
        node.visited = True
        for target_node in node.target_nodes:
            if not target_node.visited:
                self.fill_order(target_node, stack)
        stack.append(node.label)

    def DFS(self, node):
        node.visited = True
        for target_node in node.target_nodes:
            if not target_node.visited:
                self.DFS(target_node)

    def num_strongly_connected_components(self):
        stack = []

        for node in self.nodes.values():
            if not node.visited:
                self.fill_order(node, stack)

        result = 0
        while stack:
            node_label = stack.pop()
            r_node = self.rev_nodes[node_label]
            if not r_node.visited:
                self.DFS(r_node)
                result += 1
        return result


if __name__ == "__main__":
    '''
    Given: A simple directed graph with n≤103 vertices in the edge list format.
    Return: The number of strongly connected components in the graph.
    '''
    input_lines = sys.stdin.read().splitlines()
    num_vertices, num_edges = [int(x) for x in input_lines[0].split()]
    edge_list = [[int(x) for x in line.split()] for line in input_lines[1: ]]

    G = directed_graph()
    G.construct_graph(num_vertices, edge_list)
    print(G.num_strongly_connected_components())