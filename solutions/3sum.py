import sys


def three_sum(array):
    indices = {}
    for i in range(len(array)):
        indices[array[i]] = i

    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            target = - (array[i] + array[j])
            if target in indices:
                k = indices[target]
                return i + 1, j + 1, k + 1
    return -1


if __name__ == "__main__":
    '''
    Given: A positive integer k≤20, a postive integer n≤104, and k arrays of size n containing integers from −105 to 
    105.
    Return: For each array A[1..n], output three different indices 1≤p<q<r≤n such that A[p]+A[q]+A[r]=0 if exist, and 
    "-1" otherwise.
    '''
    input_lines = sys.stdin.read().splitlines()
    k, n = [int(x) for x in input_lines[0].split()]
    arrays = [[int(x) for x in line.split()] for line in input_lines[1:]]

    for array in arrays:
        res = three_sum(array)
        if res != -1:
            print(" ".join(map(str, res)))
        else:
            print(res)
