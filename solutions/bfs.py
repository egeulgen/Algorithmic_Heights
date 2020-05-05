import sys


class directed_graph:
    def __init__(self):
        self.nodes = {}

    class node:
        def __init__(self, label):
            self.label = label
            self.target_nodes = []

    def add_node(self, label):
        node = self.node(label)
        self.nodes[label] = node

    def construct_graph(self, n, edge_list):
        for i in range(1, n + 1):
            self.add_node(i)

        for edge in edge_list:
            self.nodes[edge[0]].target_nodes.append(self.nodes[edge[1]])

    def BFS(self, label):
        distances = {}
        for v in self.nodes:
            distances[v] = -1

        distances[label] = 0
        node = self.nodes[label]
        Q = [node]
        while Q:
            u = Q.pop(0)
            for conn in u.target_nodes:
                if distances[conn.label] == -1:
                    Q.append(conn)
                    distances[conn.label] = distances[u.label] + 1
        return distances


if __name__ == "__main__":
    '''
    Given: A simple graph with n≤103 vertices in the edge list format.
    Return: The number of connected components in the graph.
    '''
    input_lines = sys.stdin.read().splitlines()
    num_vertices, num_edges = [int(x) for x in input_lines[0].split()]
    edge_list = [[int(x) for x in line.split()] for line in input_lines[1:]]

    G = directed_graph()
    G.construct_graph(num_vertices, edge_list)

    distances = G.BFS(1)
    result = []
    for i in range(1, num_vertices + 1):
        result.append(str(distances[i]))
    print(" ".join(result))
