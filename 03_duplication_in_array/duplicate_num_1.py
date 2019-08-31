# -*- encoding: utf-8 -*-


def find_duplicate_num_in_array(array):
    if not array:
        return None
    for num in array:
        if num < 0 or num >= len(array):
            return None
    i = 0
    while i < len(array):
        while i != array[i]:
            if array[array[i]] == array[i]:
                return array[i]
            temp = array[i]
            array[i] = array[array[i]]
            array[temp] = temp
        i += 1
    return -1


if __name__ == '__main__':
    print find_duplicate_num_in_array([2, 3, 1, 0, 2, 5, 3])
