import sys


def insertion_sort(array, n):
    num_swaps = 0
    for i in range(1, n):
        k = i
        while k > 0 and array[k] < array[k - 1]:
            array[k], array[k - 1] = array[k - 1], array[k]
            num_swaps += 1
            k -= 1
    return array, num_swaps


if __name__ == "__main__":
    '''
    Given: A positive integer n≤103 and an array A[1..n] of integers.
    Return: The number of swaps performed by insertion sort algorithm on A[1..n].
    '''
    input_lines = sys.stdin.read().splitlines()

    n = int(input_lines[0])
    A = [int(x) for x in input_lines[1].split()]

    result, num_swaps = insertion_sort(A, n)
    print(num_swaps)