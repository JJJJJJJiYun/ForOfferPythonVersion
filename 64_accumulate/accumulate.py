# -*- encoding: utf-8 -*-


def accumulate(n):
    return n and n + accumulate(n - 1)
