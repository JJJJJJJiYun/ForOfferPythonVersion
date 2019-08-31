# -*- encoding: utf-8 -*-


def construct_array(array):
    if not array or len(array) < 2:
        return array
    result = [1]
    for i in range(1, len(array)):
        result.append(result[i - 1] * array[i - 1])
    temp = 1
    for i in range(len(array) - 2, -1, -1):
        temp *= array[i + 1]
        result[i] *= temp
    return result


if __name__ == '__main__':
    print construct_array([1, 2, 3, 4, 5])
