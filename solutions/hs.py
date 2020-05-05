import sys


def sift_down(array, heap_size, v):
    while True:
        max_node = v
        if v * 2 + 1 < heap_size and array[v * 2 + 1] > array[max_node]:
            max_node = v * 2 + 1
        if v * 2 + 2 < heap_size and array[v * 2 + 2] > array[max_node]:
            max_node = v * 2 + 2
        if max_node == v:
            return array
        array[v], array[max_node] = array[max_node], array[v]
        v = max_node



def build_max_heap(array):
    for i in range(len(array) - 1, 0, -1):
        parent = (i - 1) // 2
        if array[i] > array[parent]:
            array[parent], array[i] = array[i], array[parent]
            sift_down(array, len(array), i)
    return array


def heap_sort(array):
    heap = build_max_heap(array)

    for heap_size in range(len(heap), 1, -1):
        heap[0], heap[heap_size - 1] = heap[heap_size - 1], heap[0]
        heap = sift_down(heap, heap_size - 1, 0)
    return heap


if __name__ == "__main__":
    '''
    Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.
    Return: A sorted array A.
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])
    array = [int(x) for x in input_lines[1].split()]

    result = heap_sort(array)
    print(" ".join(map(str, result)))
