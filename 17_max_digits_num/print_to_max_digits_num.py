# -*- encoding: utf-8 -*-


def print_one_to_max_digits_num(n):
    num = [1]
    while len(num) <= n:
        print_num(num)
        i = len(num) - 1
        while i >= 0:
            if num[i] == 9:
                num[i] = 0
            else:
                break
            i -= 1
        if i == -1:
            num.insert(0, 1)
        else:
            num[i] += 1


def print_one_to_max_digits_num_recursively(n):
    nums = []
    for i in range(0, n):
        nums.append(0)
    helper(nums, 0)


def helper(nums, index):
    if index == len(nums):
        print_num(nums)
        return
    for i in range(0, 10):
        nums[index] = i
        helper(nums, index + 1)


def print_num(num):
    index = 0
    while index < len(num) and num[index] == 0:
        index += 1
    if index == len(num):
        return
    num_str = ""
    for i in range(index, len(num)):
        num_str += str(num[i])
    print num_str


if __name__ == '__main__':
    print_one_to_max_digits_num(4)
    print_one_to_max_digits_num_recursively(3)
