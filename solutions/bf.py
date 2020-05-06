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
        for i in range(1, n + 1):
            self.add_node(i)

        for edge in edge_list:
            self.nodes[edge[0]].edge_tuples.append((self.nodes[edge[1]], edge[2]))

    def Bellman_Ford(self, source=1):
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

        # proper formatting
        distances_list = []
        for label in self.nodes:
            dist = distances[label]
            if dist == float("Inf"):
                distances_list.append("x")
            else:
                distances_list.append(str(dist))
        return distances_list


if __name__ == "__main__":
    '''
    Given: A simple directed graph with integer edge weights from −103 to 103 and n≤103 vertices in the edge list 
    format.
    Return: An array D[1..n] where D[i] is the length of a shortest path from the vertex 1 to the vertex i (D[1]=0). If 
    i is not reachable from 1 set D[i] to x.
    '''
    input_lines = sys.stdin.read().splitlines()
    num_vertices, num_edges = [int(x) for x in input_lines[0].split()]
    edge_list = [[int(x) for x in line.split()] for line in input_lines[1:]]

    G = directed_graph()
    G.construct_graph(num_vertices, edge_list)
    print(" ".join(G.Bellman_Ford()))
