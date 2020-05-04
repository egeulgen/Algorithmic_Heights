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


def merge_sort(array):
    if len(array) == 1:
        return array
    if len(array) == 2:
        if array[0] < array[1]:
            return array
        return array[::-1]

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    sorted_array = merge(left, right)

    return sorted_array


if __name__ == "__main__":
    '''
    Given: A positive integer n≤105 and a sorted array A[1..n] of integers from −105 to 105, a positive integer m≤105 
    and a sorted array B[1..m] of integers from −105 to 105.
    Return: A sorted array C[1..n+m] containing all the elements of A and B.
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])
    A = [int(x) for x in input_lines[1].split()]

    result = merge_sort(A)
    print(" ".join(map(str, result)))
