# -*- encoding: utf-8 -*-


def find_duplicate_num_without_editing_array(array):
    if not array:
        return 0
    for num in array:
        if num < 1 or num > len(array) - 1:
            return 0
    start = 1
    end = len(array) - 1
    while start <= end:
        mid = (start + end) >> 1
        count = count_num_between_m_n(start, mid, array)
        if start == end:
            if count > 1:
                return start
            else:
                break
        # 说明重复部分在 start~mid
        if count > mid - start + 1:
            end = mid
        else:
            start = mid + 1
    return 0


def count_num_between_m_n(m, n, array):
    count = 0
    for num in array:
        if m <= num <= n:
            count += 1
    return count


if __name__ == '__main__':
    print find_duplicate_num_without_editing_array([1, 5, 2, 4, 5, 2])
