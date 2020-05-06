import sys


class directed_graph:

    def __init__(self):
        self.nodes = {}
        self.edges = []

    class node:
        def __init__(self, label):
            self.label = label
            self.edge_tuples = []

    def add_node(self, label):
        node = self.node(label)
        self.nodes[label] = node

    def construct_graph(self, n, edge_list):
        for i in range(1, n + 1):
            self.add_node(i)

        for edge in edge_list:
            self.nodes[edge[0]].edge_tuples.append((self.nodes[edge[1]], edge[2]))
            self.edges.append((edge[0], edge[1], edge[2]))

    def Dijkstra(self, source=1):
        distances = {}
        for v in self.nodes:
            distances[v] = float("Inf")
        distances[source] = 0

        Q = []
        for v in self.nodes:
            Q.append(v)

        while Q:
            u = min((v for v in Q), key=lambda x: distances[x])
            Q.remove(u)
            for v, weight in self.nodes[u].edge_tuples:
                new_len = distances[u] + weight
                if distances[v.label] > new_len:
                    distances[v.label] = new_len
        return distances

    def shortest_cycle_exists(self):
        dists = self.Dijkstra(self.edges[0][1])
        if dists[self.edges[0][0]] == float("Inf"):
            return "-1"
        else:
            return str(dists[self.edges[0][0]] + self.edges[0][2])


if __name__ == "__main__":
    '''
    Given: A positive integer k≤20 and k simple directed graphs with positive integer edge weights and at most 103 
    vertices in the edge list format.
    Return: For each graph, output the length of a shortest cycle going through the first specified edge if there is a 
    cycle and "-1" otherwise.
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
        result.append(G.shortest_cycle_exists())
    print(" ".join(result))
