import sys


def create_heap(array):
    heap = [0]
    for val in array:
        heap.append(val)
        index = len(heap) - 1
        while heap[index // 2] < heap[index] and index // 2 > 0:
            heap[index], heap[index // 2] = heap[index // 2], heap[index]
            index = index // 2
    return heap[1:]



if __name__ == "__main__":
    '''
    Given: A positive integer n≤105 and array A[1..n] of integers from −105 to 105.
    Return: A permuted array A satisfying the binary max heap property: for any 2≤i≤n, A[⌊i/2⌋]≥A[i].
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])
    array = [int(x) for x in input_lines[1].split()]

    result = create_heap(array)
    print(" ".join(map(str, result)))
