# -*- encoding: utf-8 -*-


def find_two_num_appear_once(array):
    xor_result = 0
    for num in array:
        xor_result ^= num
    flag = 1
    while xor_result & 1 == 0:
        flag <<= 1
        xor_result >>= 1
    num1 = 0
    num2 = 0
    for num in array:
        if num & flag == flag:
            num1 ^= num
        else:
            num2 ^= num
    return num1, num2


def find_num_appear_once(array):
    bits = []
    for i in range(0, 32):
        bits.append(0)
    for num in array:
        for i in range(0, len(bin(num))):
            if num >> i == 1:
                bits[31 - i] += 1
    result = ''
    for num in bits:
        result += str(num % 3)
    return int(result, 2)


if __name__ == '__main__':
    print find_two_num_appear_once([2, 4, 3, 6, 3, 2, 5, 5])
    print find_num_appear_once([2])
