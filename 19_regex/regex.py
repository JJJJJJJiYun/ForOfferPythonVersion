# -*- encoding: utf-8 -*-


def regex(string, pattern):
    # 两个都结束了
    if not string and not pattern:
        return True
    # string 没结束但 pattern 结束了
    if string and not pattern:
        return False
    # 有 * 的情况
    if len(pattern) > 1 and pattern[1] == '*':
        # 当前字符满足 * 前的字符，可能出现三种情况:
        # 1. * 结束了
        # 2. * 没结束，后面的字符还需要满足 *
        # 3. 这个字符也不属于 *
        if string and (pattern[0] == string[0] or pattern[0] == '.'):
            return regex(string[1:], pattern[2:]) or \
                   regex(string[1:], pattern) or \
                   regex(string, pattern[2:])
        # 当前字符不满足 * 的字符，那么一定是 * 出现 0 次
        else:
            return regex(string, pattern[2:])
    # 无 * 的情况，那么要么字符相等要么是 .
    if string and (pattern[0] == string[0] or pattern[0] == '.'):
        return regex(string[1:], pattern[1:])
    return False


if __name__ == '__main__':
    print regex("", ".")
