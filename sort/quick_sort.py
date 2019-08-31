# -*- encoding: utf-8 -*-


def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)


def quick_sort_helper(array, start, end):
    if start > end:
        return
    index = get_index(array, start, end)
    quick_sort_helper(array, start, index - 1)
    quick_sort_helper(array, index + 1, end)


def get_index(array, start, end):
    pivot = array[start]
    while start < end:
        while start < end and array[end] >= pivot:
            end -= 1
        array[start] = array[end]
        while start < end and array[start] <= pivot:
            start += 1
        array[end] = array[start]
    array[start] = pivot
    return start


if __name__ == '__main__':
    test = [3, 4, 2, 6, 1, 5]
    quick_sort(test)
    for num in test:
        print num,
