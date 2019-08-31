# -*- encoding: utf-8 -*-


def power(base, exponent):
    if base == 0:
        return 0
    if exponent == 0:
        return 1
    negative = exponent < 0
    odd = exponent & 1 == 1
    exponent = abs(exponent) - 1 if odd else abs(exponent)
    i = 1
    result = base
    while i < exponent:
        result *= result
        i <<= 1
    if odd:
        result *= base
    return 1.0 / result if negative else result


if __name__ == '__main__':
    print power(2, -8)
