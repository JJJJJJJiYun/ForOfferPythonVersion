# -*- encoding: utf-8 -*-


def count_one_of_binary_num(num):
    count = 0 if num >= 0 else 1
    num = abs(num)
    while num > 0:
        if num & 1:
            count += 1
        num >>= 1
    return count


def count_one_of_binary_num_with_math(num):
    count = 0 if num >= 0 else 1
    num = abs(num)
    while num:
        num = (num - 1) & num
        count += 1
    return count


if __name__ == '__main__':
    print count_one_of_binary_num(-5)
    print count_one_of_binary_num_with_math(-5)
