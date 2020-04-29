import sys


def fib(n):
    if n == 0:
        return 0
    fib_list = [0, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list[n]


if __name__ == "__main__":
    '''
    Given: A positive integer n≤25.
    Return: The value of Fn.
    '''
    n = int(sys.stdin.read().splitlines()[0])

    print(fib(n))