# -*- encoding: utf-8 -*-


def is_sequence_of_bst(sequence, start, end):
    if start >= end:
        return True
    index = start
    while index < end and sequence[index] < sequence[end]:
        index += 1
    for i in range(index, end):
        if sequence[i] < sequence[end]:
            return False
    return is_sequence_of_bst(sequence, start, index - 1) and \
           is_sequence_of_bst(sequence, index, end - 1)


if __name__ == '__main__':
    test = [1, 2, 3, 4, 5]
    print is_sequence_of_bst(test, 0, len(test) - 1)
