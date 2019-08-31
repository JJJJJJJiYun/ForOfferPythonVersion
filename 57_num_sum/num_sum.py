# -*- encoding: utf-8 -*-


def find_two_nums_sum_equals_s(array, s):
    if not array or len(array) < 2:
        return None
    start = 0
    end = len(array) - 1
    while start < end:
        if array[start] + array[end] == s:
            return array[start], array[end]
        if array[start] + array[end] < s:
            start += 1
        else:
            end -= 1
    return None


def print_sequence_sum_equals_s(s):
    if s < 3:
        print s
    i = 1
    j = 2
    sequence_sum = 3
    while i <= s / 2:
        if sequence_sum == s:
            for k in range(i, j + 1):
                print k,
            print ""
            j += 1
            sequence_sum += j
        elif sequence_sum < s:
            j += 1
            sequence_sum += j
        else:
            sequence_sum -= i
            i += 1


if __name__ == '__main__':
    print find_two_nums_sum_equals_s([1, 2, 4, 7, 11, 15], 15)
    print_sequence_sum_equals_s(5)
