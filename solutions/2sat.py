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

    def construct_2sat_graph(self, n, edge_list):
        for idx in range(1, n + 1):
            self.add_node(idx)
            self.add_node(-idx)

        for edge in edge_list:
            self.nodes[-edge[0]].target_nodes.append(self.nodes[edge[1]])
            self.nodes[-edge[1]].target_nodes.append(self.nodes[edge[0]])

            self.rev_nodes[edge[1]].target_nodes.append(self.rev_nodes[-edge[0]])
            self.rev_nodes[edge[0]].target_nodes.append(self.rev_nodes[-edge[1]])

    def fill_order(self, node, stack):
        node.visited = True
        for target_node in node.target_nodes:
            if not target_node.visited:
                self.fill_order(target_node, stack)
        stack.append(node.label)

    def DFS(self, node, scc):
        node.visited = True
        scc.append(node.label)
        for target_node in node.target_nodes:
            if not target_node.visited:
                self.DFS(target_node, scc)

    def strongly_connected_components(self):
        stack = []
        for node in self.nodes.values():
            if not node.visited:
                self.fill_order(node, stack)

        all_scc = []
        scc = []
        while stack:
            node_label = stack.pop()
            r_node = self.rev_nodes[node_label]
            if not r_node.visited:
                self.DFS(r_node, scc)
                all_scc.append(scc[:])
                scc = []
        return all_scc

    def is_2_Sat(self):
        all_scc = self.strongly_connected_components()
        assignments = {}
        for comp in all_scc:
            for v in comp:
                if -v in comp:
                    return False
                if abs(v) not in assignments:
                    assignments[abs(v)] = -v
        return assignments


if __name__ == "__main__":
    '''
    Given: A positive integer k≤20 and k 2SAT formulas represented as follows. The first line gives the number of 
    variables n≤103 and the number of clauses m≤104, each of the following m lines gives a clause of length 2 by 
    specifying two different literals: e.g., a clause (x3∨x⎯⎯⎯5) is given by 3 -5.
    Return: For each formula, output 0 if it cannot be satisfied or 1 followed by a satisfying assignment otherwise.
    '''
    sys.setrecursionlimit(10 ** 6)

    input_lines = sys.stdin.read().splitlines()
    k = int(input_lines[0])

    i = 2
    n_var_list = []
    edge_lists = []
    while i < len(input_lines):
        num_vars, num_clauses = [int(x) for x in input_lines[i].split()]
        n_var_list.append(num_vars)
        edge_lists.append([[int(x) for x in line.split()] for line in input_lines[i + 1: i + 1 + num_clauses]])
        i = i + 1 + num_clauses + 1

    for num_vars, edge_list in zip(n_var_list, edge_lists):
        G = directed_graph()
        G.construct_2sat_graph(num_vars, edge_list)
        res_dict = G.is_2_Sat()
        if res_dict:
            result = []
            for i in range(1, num_vars + 1):
                result.append(res_dict[i])
            print("1 " + " ".join(map(str, result)))
        else:
            print(0)