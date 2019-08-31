# -*- encoding: utf-8 -*-


def get_last_num_in_circle(n, m):
    if n == 0 or m == 0:
        return -1
    array = []
    for i in range(0, n):
        array.append(i)
    i = 0
    while len(array) > 1:
        if i == len(array):
            i = 0
        count_m = 1
        while count_m < m:
            i += 1
            if i == len(array):
                i = 0
            count_m += 1
        array.pop(i)
    return array[0]


if __name__ == '__main__':
    print get_last_num_in_circle(6, 6)
