# -*- encoding: utf-8 -*-


def fibonacci_with_recursion(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    former, latter, result = 0, 1, 0
    for i in range(1, n):
        result = former + latter
        former = latter
        latter = result
    return result


if __name__ == '__main__':
    print fibonacci(3)
