import sys
from random import choice


def selection(array, k):
    pivot = choice(array)
    left = []
    mid = []
    right = []
    for elem in array:
        if elem < pivot:
            left.append(elem)
        elif elem == pivot:
            mid.append(elem)
        else:
            right.append(elem)

    if k <= len(left):
        return selection(left, k)
    if len(left) < k <= len(left) + len(mid):
        return pivot
    return selection(right, k - (len(left) + len(mid)))


if __name__ == "__main__":
    '''
    Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105, a positive number k≤n.
    Return: The k-th smallest element of A.
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])
    A = [int(x) for x in input_lines[1].split()]
    k = int(input_lines[2])

    print(selection(A, k))
