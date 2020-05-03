import sys


def merge(array_A, array_B):
    merged_array = []
    i = 0
    j = 0
    while i < len(array_A) and j < len(array_B):
        if array_A[i] < array_B[j]:
            merged_array.append(array_A[i])
            i += 1
        else:
            merged_array.append(array_B[j])
            j += 1
    if i == len(array_A):
        for k in array_B[j:]:
            merged_array.append(k)
    else:
        for k in array_A[i:]:
            merged_array.append(k)
    return merged_array


if __name__ == "__main__":
    '''
    Given: A positive integer n≤105 and a sorted array A[1..n] of integers from −105 to 105, a positive integer m≤105 
    and a sorted array B[1..m] of integers from −105 to 105.
    Return: A sorted array C[1..n+m] containing all the elements of A and B.
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])
    m = int(input_lines[2])
    A = [int(x) for x in input_lines[1].split()]
    B = [int(x) for x in input_lines[3].split()]

    result = merge(A, B)
    print(" ".join(map(str, result)))
