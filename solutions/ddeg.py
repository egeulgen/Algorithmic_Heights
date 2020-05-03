import sys


if __name__ == "__main__":
    '''
    Given: A simple graph with n≤103 vertices in the edge list format.
    Return: An array D[1..n] where D[i] is the degree of vertex i.
    '''
    input_lines = sys.stdin.read().splitlines()
    num_vertices, num_edges = [int(x) for x in input_lines[0].split()]
    edge_list = input_lines[1:]

    degree_dict = {}
    ddeg_dict = {}
    for i in range(1, num_vertices + 1):
        degree_dict[i] = 0
        ddeg_dict[i] = 0

    for edge in edge_list:
        v1, v2 = [int(x) for x in edge.split()]
        degree_dict[v1] += 1
        degree_dict[v2] += 1

    for edge in edge_list:
        v1, v2 = [int(x) for x in edge.split()]
        ddeg_dict[v1] += degree_dict[v2]
        ddeg_dict[v2] += degree_dict[v1]

    result = []
    for i in range(1, num_vertices + 1):
        result.append(str(ddeg_dict[i]))

    print(" ".join(result))
