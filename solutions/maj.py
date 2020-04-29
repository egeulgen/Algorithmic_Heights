import sys


if __name__ == "__main__":
    '''
    Given: A positive integer k≤20, a positive integer n≤104, and k arrays of size n containing positive integers not 
    exceeding 105.
    Return: For each array, output an element of this array occurring strictly more than n/2 times if such element 
    exists, and "-1" otherwise.
    '''
    input_lines = sys.stdin.read().splitlines()
    k, n = map(int, input_lines[0].split())
    arrays = []
    for i in range(1, k + 1):
        arrays.append([int(x) for x in input_lines[i].split()])

    result = []
    for arr in arrays:
        res = -1
        all_items = set(arr)
        for item in all_items:
            if arr.count(item) > n // 2:
                res = item
                break
        result.append(str(res))

    print(" ".join(result))