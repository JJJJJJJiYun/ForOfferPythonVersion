# -*- encoding: utf-8 -*-


def get_first_appear_once_ch(string):
    count_dict = {}
    for ch in string:
        if ch in count_dict:
            count_dict[ch] += 1
        else:
            count_dict[ch] = 1
    for ch in string:
        if count_dict[ch] == 1:
            return ch


if __name__ == '__main__':
    print get_first_appear_once_ch("acbaeegfgfh")
