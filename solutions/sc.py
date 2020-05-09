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

    def is_semi_connected(self):
        all_distances = {}
        for label in self.nodes:
            all_distances[label] = self.BFS(label)

        for i in range(1, len(self.nodes)):
            for j in range(i, len(self.nodes) + 1):
                if all_distances[i][j] == -1 and all_distances[j][i] == -1:
                    return "-1"
        return "1"


if __name__ == "__main__":
    '''
    Given: A positive integer k≤20 and k simple directed graphs with at most 103 vertices and 2⋅103 edges each in the 
    edge list format.
    Return: For each graph, output a vertex from which all other vertices are reachable (if such a vertex exists) and 
    "-1" otherwise.
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
        result.append(G.is_semi_connected())
    print(" ".join(result))
