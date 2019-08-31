# -*- encoding: utf-8 -*-


def get_max_gifts_value(matrix):
    if not matrix or not matrix[0]:
        return 0
    dp = []
    value = 0
    for num in matrix[0]:
        value += num
        dp.append(value)
    for i in range(1, len(matrix)):
        dp[0] += matrix[i][0]
        for j in range(1, len(matrix[0])):
            dp[j] = max(dp[j - 1], dp[j]) + matrix[i][j]
    return dp[len(matrix[0])-1]


if __name__ == '__main__':
    print get_max_gifts_value(
        [[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]])
