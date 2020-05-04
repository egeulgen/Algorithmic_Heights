import sys


def two_sum(array):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == 0:
                return i + 1, j + 1
    return -1


if __name__ == "__main__":
    '''
    Given: A positive integer k≤20, a positive integer n≤104, and k arrays of size n containing integers from −105 to 105.
    Return: For each array A[1..n], output two different indices 1≤p<q≤n such that A[p]=−A[q] if exist, and "-1" otherwise.
    '''
    input_lines = sys.stdin.read().splitlines()
    k, n = [int(x) for x in input_lines[0].split()]
    arrays = [[int(x) for x in line.split()] for line in input_lines[1:]]

    for array in arrays:
        res = two_sum(array)
        if res != -1:
            print(" ".join(map(str, res)))
        else:
            print(res)
