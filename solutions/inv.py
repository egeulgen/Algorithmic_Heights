import sys


def merge_count(array_A, array_B):
    merged_array = []
    count = 0
    i, j = 0, 0
    while i < len(array_A) and j < len(array_B):
        if array_A[i] <= array_B[j]:
            merged_array.append(array_A[i])
            i += 1
        else:
            merged_array.append(array_B[j])
            count += len(array_A) - i
            j += 1
    merged_array += array_A[i:] + array_B[j:]
    return merged_array, count


def merge_sort_count(array):
    if len(array) <= 1:
        return array, 0

    mid = len(array) // 2

    left, count_l = merge_sort_count(array[:mid])
    right, count_r = merge_sort_count(array[mid:])

    sorted_array, count_m = merge_count(left, right)

    return sorted_array, count_l + count_r + count_m


if __name__ == "__main__":
    '''
    Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.
    Return: The number of inversions in A.
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])
    array = [int(x) for x in input_lines[1].split()]

    print(merge_sort_count(array)[1])
