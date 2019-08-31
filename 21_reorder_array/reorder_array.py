# -*- encoding: utf-8 -*-


def reorder_array(array):
    if not array:
        return
    i, j = 0, len(array) - 1
    while i < j:
        while i < j and array[i] & 1 == 1:
            i += 1
        while i < j and array[j] & 1 == 0:
            j -= 1
        if i < j:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp


if __name__ == '__main__':
    test_array = [2, 1, 4, 8, 7, 7, 5, 6, 3]
    reorder_array(test_array)
    print test_array
