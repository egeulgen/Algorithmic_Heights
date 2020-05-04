import sys


def two_way_partition(array):
    pivot = array[0]
    left = []
    right = []
    for elem in array[1:]:
        if elem <= pivot:
            left.append(elem)
        else:
            right.append(elem)
    return left + [pivot] + right


if __name__ == "__main__":
    '''
    Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.
    Return: A permuted array B[1..n] such that it is a permutation of A and there is an index 1≤q≤n such that B[i]≤A[1] 
    for all 1≤i≤q−1, B[q]=A[1], and B[i]>A[1] for all q+1≤i≤n.
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])
    array = [int(x) for x in input_lines[1].split()]

    result = two_way_partition(array)
    print(" ".join(map(str, result)))
