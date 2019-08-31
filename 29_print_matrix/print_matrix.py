# -*- encoding: utf-8 -*-


def print_matrix(matrix, rows, cols, row, col):
    if rows <= 0 or cols <= 0:
        return
    for i in range(col, col + cols):
        print matrix[row][i]
    if rows > 1:
        for i in range(row + 1, row + rows):
            print matrix[i][row + rows - 1]
        if cols > 1:
            for i in range(col + cols - 2, col - 1, -1):
                print matrix[row + rows - 1][i]
            if rows > 2:
                for i in range(row + rows - 2, row, -1):
                    print matrix[i][row]
    print_matrix(matrix, rows - 2, cols - 2, row + 1, col + 1)


def generate_matrix(m, n):
    matrix = []
    num = 1
    for i in range(0, m):
        matrix.append([])
        for j in range(0, n):
            matrix[i].append(num)
            num += 1
    return matrix


if __name__ == '__main__':
    matrix = generate_matrix(3, 3)
    print_matrix(matrix, 3, 3, 0, 0)
