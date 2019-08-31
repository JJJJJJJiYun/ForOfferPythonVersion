# -*- encoding: utf-8 -*-


def add(a, b):
    while b != 0:
        s = a ^ b
        carry = (a & b) << 1
        a = s
        b = carry
    return a


if __name__ == '__main__':
    print add(1, 2)
