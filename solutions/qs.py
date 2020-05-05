import sys
from random import randint

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


def quick_sort(array):
    if len(array) in [0, 1]:
        return array
    if len(array) == 2:
        if array[0] < array[1]:
            return array
        return array[::-1]

    pivot_idx = randint(0, len(array) - 1)
    left = quick_sort(array[:pivot_idx])
    right = quick_sort(array[pivot_idx:])

    sorted_array = merge(left, right)

    return sorted_array


if __name__ == "__main__":
    '''
    Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.
    Return: A sorted array A[1..n].
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])
    A = [int(x) for x in input_lines[1].split()]

    result = quick_sort(A)
    print(" ".join(map(str, result)))
