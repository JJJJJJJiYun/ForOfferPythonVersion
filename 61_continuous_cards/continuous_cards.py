# -*- encoding: utf-8 -*-


def is_continuous_cards(array):
    if len(array) != 5:
        return False
    array.sort()
    i = 0
    count_zero = 0
    while array[i] == 0:
        count_zero += 1
        i += 1
    gap = 0
    i += 1
    while i < len(array):
        if array[i] == array[i - 1]:
            return False
        gap += array[i] - array[i - 1] - 1
        i += 1
    return gap <= count_zero


if __name__ == '__main__':
    print is_continuous_cards([1, 0, 0, 49, 0])
