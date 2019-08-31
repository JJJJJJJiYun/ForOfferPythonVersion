# -*- encoding: utf-8 -*-


def reverse_sentence(sentence):
    sentence = list(sentence)
    reverse(sentence, 0, len(sentence) - 1)
    start = 0
    for i in range(0, len(sentence)):
        if sentence[i] == ' ':
            reverse(sentence, start, i - 1)
            start = i + 1
    return "".join(sentence)


def left_rotate_string(sentence, n):
    sentence = list(sentence)
    reverse(sentence, 0, n - 1)
    reverse(sentence, n, len(sentence) - 1)
    reverse(sentence, 0, len(sentence) - 1)
    return "".join(sentence)


def reverse(sentence, start, end):
    i = start
    j = end
    while i < j:
        temp = sentence[i]
        sentence[i] = sentence[j]
        sentence[j] = temp
        i += 1
        j -= 1


if __name__ == '__main__':
    print reverse_sentence("i am a student.")
    print left_rotate_string("abcdefg", 2)
