import sys


class graph:
    def __init__(self):
        self.nodes = {}

    class node:
        def __init__(self, label):
            self.label = label
            self.connected_nodes = []
            self.visited = False

    def add_node(self, label):
        node = self.node(label)
        self.nodes[label] = node

    def construct_graph(self, n, edge_list):
        for i in range(1, n + 1):
            self.add_node(i)

        for edge in edge_list:
            self.nodes[edge[0]].connected_nodes.append(self.nodes[edge[1]])
            self.nodes[edge[1]].connected_nodes.append(self.nodes[edge[0]])

    def explore(self, node):
        node.visited = True
        for node2 in node.connected_nodes:
            if not node2.visited:
                self.explore(node2)

    def connected_components_DFS(self):
        count_conn_comps = 0
        for node in self.nodes.values():
            if not node.visited:
                self.explore(node)
                count_conn_comps += 1
        return count_conn_comps


if __name__ == "__main__":
    '''
    Given: A simple graph with n≤103 vertices in the edge list format.
    Return: The number of connected components in the graph.
    '''
    input_lines = sys.stdin.read().splitlines()
    num_vertices, num_edges = [int(x) for x in input_lines[0].split()]
    edge_list = [[int(x) for x in line.split()] for line in input_lines[1:]]

    G = graph()
    G.construct_graph(num_vertices, edge_list)
    print(G.connected_components_DFS())
