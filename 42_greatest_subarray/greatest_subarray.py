# -*- encoding: utf-8 -*-


def find_greatest_subarray(array):
    if not array:
        return 0
    if len(array) == 1:
        return array[0]
    current_sum = array[0]
    max_sum = current_sum
    for i in range(1, len(array)):
        if current_sum < 0:
            current_sum = 0
        current_sum += array[i]
        max_sum = max(max_sum, current_sum)
    return max_sum

# 这个方法其实和上面的是一样的，只不过这个记录了每前 i 项的最大值
def find_greatest_subarray_with_dp(array):
    if not array:
        return 0
    if len(array) == 1:
        return array[0]
    dp = [array[0]]
    for i in range(1, len(array)):
        dp.append(array[i] if dp[i - 1] < 0 else dp[i - 1] + array[i])
    max_result = dp[0]
    for num in dp:
        max_result = max(num, max_result)
    return max_result


if __name__ == '__main__':
    print find_greatest_subarray([1, -2, 3, 10, -4, 7, 2, -5])
    print find_greatest_subarray_with_dp([1, -2, 3, 10, -4, 7, 2, -5])
