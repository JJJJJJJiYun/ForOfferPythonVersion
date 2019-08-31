# -*- encoding: utf-8 -*-


def count_num_sorted_array(array, num):
    if not array:
        return 0
    last = get_index_of_last_occurrence(array, num)
    first = get_index_of_first_occurrence(array, num)
    if first == -1 or last == -1:
        return 0
    return last - first + 1


def get_index_of_first_occurrence(array, num):
    start = 0
    end = len(array) - 1
    while start <= end:
        middle = (start + end) >> 1
        if array[middle] < num:
            start = middle + 1
        elif array[middle] > num:
            end = middle - 1
        else:
            if middle - 1 < 0 or array[middle - 1] != array[middle]:
                return middle
            else:
                end = middle - 1
    return -1


def get_index_of_last_occurrence(array, num):
    start = 0
    end = len(array) - 1
    while start <= end:
        middle = (start + end) >> 1
        if array[middle] < num:
            start = middle + 1
        elif array[middle] > num:
            end = middle - 1
        else:
            if middle + 1 >= len(array) or array[middle + 1] != array[middle]:
                return middle
            else:
                start = middle + 1
    return -1


def find_missing_num_in_sorted_array(array):
    if not array:
        return -1
    start = 0
    end = len(array) - 1
    while start <= end:
        middle = (start + end) >> 1
        if array[middle] == middle:
            start = middle + 1
        else:
            if middle - 1 < 0 or array[middle - 1] == middle - 1:
                return middle
            end = middle - 1
    return -1


def find_num_equals_index(array):
    if not array:
        raise RuntimeError("错误的数组")
    start = 0
    end = len(array) - 1
    while start <= end:
        middle = (start + end) >> 1
        if array[middle] == middle:
            return middle
        if array[middle] < middle:
            start = middle + 1
        else:
            end = middle - 1
    return -1


if __name__ == '__main__':
    print count_num_sorted_array([1, 2, 3, 3, 3, 4, 5, 6], 3)
    print find_missing_num_in_sorted_array([0, 1, 2, 4, 5, 6])
    print find_num_equals_index([-3, -1, 1, 3, 5])
