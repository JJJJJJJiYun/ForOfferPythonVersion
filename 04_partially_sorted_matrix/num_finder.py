# -*- encoding: utf-8 -*-


def find_num_in_partially_sorted_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    i = 0
    j = len(matrix[0]) - 1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            j -= 1
        else:
            i += 1
    return False


if __name__ == '__main__':
    print find_num_in_partially_sorted_matrix(
        [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], 7)
