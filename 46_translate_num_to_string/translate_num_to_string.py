# -*- encoding: utf-8 -*-


def translate_num_to_string(array):
    if not array:
        return 0
    if len(array) == 1:
        return 1
    dp = []
    for i in range(0, len(array) + 1):
        dp.append(0)
    dp[len(array)] = 0
    dp[len(array) - 1] = 1
    for i in range(len(array) - 2, -1, -1):
        if 0 <= int(str(array[i]) + str(array[i + 1])) <= 25:
            dp[i] = dp[i + 1] + dp[i + 2]
        else:
            dp[i] = dp[i + 1]
    return dp[0]


if __name__ == '__main__':
    print translate_num_to_string([1, 2, 2, 5, 8])
