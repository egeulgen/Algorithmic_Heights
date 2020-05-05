import sys


class undirected_graph:
    def __init__(self):
        self.nodes = {}
        self.adj_mat = {}

    class node:
        def __init__(self, label):
            self.label = label
            self.target_nodes = []

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
            self.nodes[edge[1]].target_nodes.append(self.nodes[edge[0]])

        self.construct_adj_matrix()

    def construct_adj_matrix(self):
        adj_mat = [[0 for _ in range(len(self.nodes))] for _ in range(len(self.nodes))]
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                if j + 1 in [v.label for v in self.nodes[i + 1].target_nodes]:
                    adj_mat[i][j] = 1
                    adj_mat[j][i] = 1
        self.adj_mat = adj_mat

    def BFS_2_coloring(self, label):
        colors = {}
        for v in self.nodes:
            colors[v] = None

        colors[label] = "red"
        node = self.nodes[label]
        Q = [node]
        while Q:
            u = Q.pop(0)
            for conn in u.target_nodes:
                if colors[conn.label] == colors[u.label]:
                    return False
                if colors[conn.label] is None:
                    Q.append(conn)
                    colors[conn.label] = "blue" if colors[u.label] == "red" else "red"
        return True

    def is_bipartite(self):
        for label in self.nodes:
            if not self.BFS_2_coloring(label):
                return "-1"
        return "1"



if __name__ == "__main__":
    '''
    Given: A positive integer k≤20 and k simple graphs in the edge list format with at most 103 vertices each.
    Return: For each graph, output "1" if it is bipartite and "-1" otherwise.
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
        G = undirected_graph()
        G.construct_graph(num_vertices, edge_list)
        result.append(G.is_bipartite())
    print(" ".join(result))
