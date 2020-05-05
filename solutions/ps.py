import sys
from qs import quick_sort


if __name__ == "__main__":
    '''
    Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105, a positive integer k≤1000.
    Return: The k smallest elements of a sorted array A.
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])
    A = [int(x) for x in input_lines[1].split()]
    k = int(input_lines[2])

    A = quick_sort(A)
    result = [A[i] for i in range(k)]
    print(" ".join(map(str, result)))
