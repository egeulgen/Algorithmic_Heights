import sys


def binary_search(array, item):
    beg = 0
    end = len(array) - 1
    found = False
    pos = -1
    while beg <= end and not found:
        mid = (beg + end) // 2
        if item == array[mid]:
            found = True
            pos = mid
        else:
            if item < array[mid]:
                end = mid - 1
            else:
                beg = mid + 1
    return pos


if __name__ == "__main__":
    '''
    Given: Two positive integers n≤105 and m≤105, a sorted array A[1..n] of integers from −105 to 105 and a list of m 
    integers −105≤k1,k2,…,km≤105.
    Return: For each ki, output an index 1≤j≤n s.t. A[j]=ki or "-1" if there is no such index.
    '''
    input_lines = sys.stdin.read().splitlines()

    n = int(input_lines[0])
    m = int(input_lines[1])
    A = [int(x) for x in input_lines[2].split()]

    result = []
    for item in [int(x) for x in input_lines[3].split()]:
        res = binary_search(A, item)
        if res != -1:
            res += 1
        result.append(str(res))

    print(" ".join(result))