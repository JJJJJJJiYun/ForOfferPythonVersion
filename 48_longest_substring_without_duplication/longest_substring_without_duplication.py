# -*- encoding: utf-8 -*-


def get_longest_substring_without_duplication(string):
    chs = []
    for i in range(0, 26):
        chs.append(-1)
    current_length = 0
    max_length = 0
    for i, ch in enumerate(string):
        pre_index = chs[ord(ch) - ord('a')]
        if pre_index == -1 or i - pre_index > current_length:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = i - pre_index
        chs[ord(ch) - ord('a')] = i
    return max(max_length, current_length)


if __name__ == '__main__':
    print get_longest_substring_without_duplication("abcacfrar")
