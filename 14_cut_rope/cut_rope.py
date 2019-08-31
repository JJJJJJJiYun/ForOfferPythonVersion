# -*- encoding: utf-8 -*-


def cut_rope(n):
    if n <= 0:
        return 0
    dp = [0, 1, 2, 3]
    for i in range(4, n + 1):
        result = 0
        for j in range(1, i / 2 + 1):
            if dp[j] * dp[i - j] > result:
                result = dp[j] * dp[i - j]
        dp.append(result)
    return dp[n]


if __name__ == '__main__':
    print cut_rope(4)
