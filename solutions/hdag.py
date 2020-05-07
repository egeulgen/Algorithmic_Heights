import sys


class directed_graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []
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
            self.edges.append((edge[0], edge[1]))

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

    def Hamiltonian_path(self):
        t_sorting = self.topological_sorting()
        path = []
        for i in range(len(t_sorting)):
            if i == len(t_sorting) - 1:
                path.append(t_sorting[i])
            elif (t_sorting[i], t_sorting[i + 1]) in self.edges:
                path.append(t_sorting[i])
            else:
                return None
        return path




if __name__ == "__main__":
    '''
    Given: A positive integer k≤20 and k simple directed acyclic graphs in the edge list format with at most 103 
    vertices each.
    Return: For each graph, if it contains a Hamiltonian path output "1" followed by a Hamiltonian path (i.e., a list of 
    vertices), otherwise output "-1".
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

    for num_vertices, edge_list in zip(n_vert_list, edge_lists):
        G = directed_graph()
        G.construct_graph(num_vertices, edge_list)
        ham_path = G.Hamiltonian_path()
        if ham_path is None:
            print(-1)
        else:
            ham_path = [1] + ham_path
            print(" ".join(map(str, ham_path)))