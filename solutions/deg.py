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
    for edge in edge_list:
        v1, v2 = [int(x) for x in edge.split()]
        if v1 in degree_dict:
            degree_dict[v1] += 1
        else:
            degree_dict[v1] = 1
        if v2 in degree_dict:
            degree_dict[v2] += 1
        else:
            degree_dict[v2] = 1

    result = []
    for i in range(1, num_vertices + 1):
        if i in degree_dict:
            result.append(str(degree_dict[i]))
        else:
            result.append("0")
    print(" ".join(result))
