# -*- encoding: utf-8 -*-
import copy


def find_inverse_pairs(array):
    copy_array = copy.copy(array)
    return helper(array, copy_array, 0, len(array) - 1)


def helper(array, copy_array, start, end):
    if start >= end:
        copy_array[start] = array[start]
        return 0
    middle = (start + end) >> 1
    left = helper(array, copy_array, start, middle)
    right = helper(array, copy_array, middle + 1, end)
    i = middle
    j = end
    k = end
    count = 0
    while i >= start and j >= middle + 1:
        if array[i] > array[j]:
            count += j - middle
            copy_array[k] = array[i]
            i -= 1
        else:
            copy_array[k] = array[j]
            j -= 1
        k -= 1
    while i >= start:
        copy_array[k] = array[i]
        i -= 1
        k -= 1
    while j >= middle + 1:
        copy_array[k] = array[j]
        j -= 1
        k -= 1
    while end > k:
        array[end] = copy_array[end]
        end -= 1
    return count + left + right


if __name__ == '__main__':
    print find_inverse_pairs([7, 5, 6, 4])
