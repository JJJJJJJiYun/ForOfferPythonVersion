# -*- encoding: utf-8 -*-
import sys


def find_min_num_in_rotated_array(array):
    if not array:
        return None
    if array[0] < array[len(array) - 1]:
        return array[0]
    left, right = 0, len(array) - 1
    while right - left > 1:
        mid = (left + right) >> 1
        if array[left] == array[mid] == array[right]:
            return find_min_in_array(array)
        if array[left] <= array[mid]:
            left = mid
        else:
            right = mid
    return array[right]


def find_min_in_array(array):
    min_num = sys.maxsize
    for num in array:
        if num < min_num:
            min_num = num
    return min_num


if __name__ == '__main__':
    print find_min_num_in_rotated_array([1, 1, 1, 0, 1])
