# -*- encoding: utf-8 -*-


def print_string_permutation(string):
    chars = []
    for i in range(0, len(string)):
        chars.append(string[i])
    helper("", len(string), chars)


def helper(current_str, length, chars):
    if len(current_str) == length:
        print current_str
    for i in range(0, len(chars)):
        ch = chars.pop(i)
        helper(current_str + ch, length, chars)
        chars.insert(i, ch)


if __name__ == '__main__':
    print_string_permutation("abc")