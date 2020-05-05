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

    def construct_adj_matrix(self):
        adj_mat = [[0 for _ in range(len(self.nodes))] for _ in range(len(self.nodes))]
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                if j + 1 in [v.label for v in self.nodes[i + 1].target_nodes]:
                    adj_mat[i][j] = 1
                    adj_mat[j][i] = 1
        self.adj_mat = adj_mat

    def DFS(self, visited, n, vert, start, count):
        visited[vert] = True
        if n == 0:
            visited[vert] = False
            if self.adj_mat[vert][start] == 1:
                count = count + 1
                return count
            else:
                return count

        for i in range(len(self.adj_mat)):
            if not visited[i] and self.adj_mat[vert][i] == 1:
                count = self.DFS(visited, n - 1, i, start, count)
        visited[vert] = False
        return count

    def count_cycles(self, n=4):
        self.construct_adj_matrix()
        visited = [False] * len(self.adj_mat)

        count = 0
        for i in range(len(self.adj_mat) - (n - 1)):
            count = self.DFS(visited, n - 1, i, i, count)
            visited[i] = True

        count = count // 2
        if count > 0:
            return "1"
        return "-1"


if __name__ == "__main__":
    '''
    Given: A positive integer k≤20 and k simple undirected graphs with n≤400 vertices in the edge list format.    
    Return: For each graph, output "1" if it contains a simple cycle (that is, a cycle which doesn’t intersect itself) 
    of length 4 and "-1" otherwise.
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
        result.append(G.count_cycles())
    print(" ".join(result))
