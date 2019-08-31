# -*- encoding: utf-8 -*-


def sort_array_for_min_num(array):
    array = sorted(array, cmp=comparator)
    result = ""
    for num in array:
        result += str(num)
    print result


def comparator(x, y):
    x = str(x)
    y = str(y)
    i = 0
    while i < len(x) or i < len(y):
        if i >= len(x):
            x += x[i - 1]
        if i >= len(y):
            y += y[i - 1]
        i += 1
    x = int(x)
    y = int(y)
    if x < y:
        return -1
    if x > y:
        return 1
    return 0


if __name__ == '__main__':
    sort_array_for_min_num([3, 32, 321])
