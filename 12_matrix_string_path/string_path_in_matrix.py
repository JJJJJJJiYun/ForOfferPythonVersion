# -*- encoding: utf-8 -*-


def find_string_path_in_matrix(matrix, string):
    if not matrix:
        return False
    visited = [[], [], []]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            visited[i].append(False)
    for i, array in enumerate(matrix):
        for j, ch in enumerate(array):
            if helper(matrix, i, j, string, 0, visited):
                return True
    return False


def helper(matrix, i, j, string, index, visited):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or \
            matrix[i][j] != string[index] or visited[i][j]:
        return False
    if index == len(string) - 1:
        return True
    visited[i][j] = True
    left = helper(matrix, i, j - 1, string, index + 1, visited)
    right = helper(matrix, i, j + 1, string, index + 1, visited)
    up = helper(matrix, i - 1, j, string, index + 1, visited)
    down = helper(matrix, i + 1, j, string, index + 1, visited)
    visited[i][j] = False
    return left or right or up or down


if __name__ == '__main__':
    print find_string_path_in_matrix(
        [['a', 'b', 't', 'g'], ['c', 'f', 'c', 's'], ['j', 'd', 'e', 'h']],
        "abfb")
