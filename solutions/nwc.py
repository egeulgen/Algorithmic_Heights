import sys


class directed_graph:
    def __init__(self):
        self.nodes = {}

    class node:
        def __init__(self, label):
            self.label = label
            self.edge_tuples = []

    def add_node(self, label):
        node = self.node(label)
        self.nodes[label] = node

    def construct_graph(self, n, edge_list):
        # add a dummy "source_node" to our graph and add an edge from source to every node with weight 0
        self.add_node(-1)
        for i in range(1, n + 1):
            self.add_node(i)
            self.nodes[-1].edge_tuples.append((self.nodes[i], 0))

        for edge in edge_list:
            self.nodes[edge[0]].edge_tuples.append((self.nodes[edge[1]], edge[2]))

    def has_negative_cycle(self, source=-1):
        distances = {}
        for v in self.nodes:
            distances[v] = float("Inf")
        distances[source] = 0

        for _ in range(len(self.nodes) - 1):
            for u in self.nodes:
                if distances[u] != float("Inf"):
                    for v, weight in self.nodes[u].edge_tuples:
                        new_len = distances[u] + weight
                        if distances[v.label] > new_len:
                            distances[v.label] = new_len

        for u in self.nodes:
            if distances[u] != float("Inf"):
                for v, weight in self.nodes[u].edge_tuples:
                    if distances[v.label] > distances[u] + weight:
                        return "1"
        return "-1"


if __name__ == "__main__":
    '''
    Given: A positive integer k≤20 and k simple directed graphs with integer edge weights from −103 to 103 and n≤103 
    vertices in the edge list format.
    Return: For each graph, output "1" if it contains a negative weight cycle and "-1" otherwise.
    '''
    input_lines = sys.stdin.read().splitlines()
    k = int(input_lines[0])

    i = 1
    n_vert_list = []
    edge_lists = []
    while i < len(input_lines):
        num_vertices, num_edges = [int(x) for x in input_lines[i].split()]
        n_vert_list.append(num_vertices)
        edge_lists.append([[int(x) for x in line.split()] for line in input_lines[i + 1: i + 1 + num_edges]])
        i = i + 1 + num_edges

    result = []
    for num_vertices, edge_list in zip(n_vert_list, edge_lists):
        G = directed_graph()
        G.construct_graph(num_vertices, edge_list)
        result.append(G.has_negative_cycle())
    print(" ".join(result))
