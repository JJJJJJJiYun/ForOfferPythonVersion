# -*- encoding: utf-8 -*-


def calculate_dices_probability(n):
    if n < 1:
        return
    dp = [[], []]
    for i in range(0, n * 6 + 1):
        dp[0].append(0)
        dp[1].append(0)
    for i in range(1, 7):
        dp[0][i] = 1
    flag = 0
    for i in range(2, n + 1):
        last_flag = flag
        flag = 1 - flag
        for j in range(0, i - 1):
            dp[last_flag][j] = 0
        for j in range(i, i * 6 + 1):
            count = 0
            k = j - 1
            while k > 0 and k >= j - 6:
                count += dp[last_flag][k]
                k -= 1
            dp[flag][j] = count
    for i in range(n, 6 * n + 1):
        print str(i) + ": " + str(float(dp[flag][i]) / pow(6, n))


if __name__ == '__main__':
    print calculate_dices_probability(4)
