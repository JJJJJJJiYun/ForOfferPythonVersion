# -*- encoding: utf-8 -*-
from sort.quick_sort import get_index


def find_more_than_half_num(array):
    if not array:
        raise RuntimeError("错误的数组")
    count = 0
    last = array[0] - 1
    for num in array:
        if count == 0:
            last = num
        if num == last:
            count += 1
        else:
            count -= 1
    return last


def find_more_than_half_num_with_partition(array):
    start = 0
    end = len(array) - 1
    while start <= end:
        index = get_index(array, start, end)
        if index < len(array) / 2:
            start = index + 1
        elif index > len(array) / 2:
            end = index - 1
        else:
            return array[index]
    raise RuntimeError("错误的数组")


if __name__ == '__main__':
    print find_more_than_half_num([1, 2, 3, 2, 2, 2, 5, 4, 2])
