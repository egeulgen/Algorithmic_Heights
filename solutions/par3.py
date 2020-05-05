import sys


def three_way_partition(array):
    pivot = array[0]
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
    return left + mid + right


if __name__ == "__main__":
    '''
    Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.
    Return: An array B[1..n] such that it is a permutation of A and there are indices 1≤q≤r≤n such that B[i]<A[1] for 
    all 1≤i≤q−1, B[i]=A[1] for all q≤i≤r, and B[i]>A[1] for all r+1≤i≤n.
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])
    array = [int(x) for x in input_lines[1].split()]

    result = three_way_partition(array)
    print(" ".join(map(str, result)))
