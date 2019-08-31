# -*- encoding: utf-8 -*-


class ComplexListNode(object):
    def __init__(self, val, nxt=None, sibling=None):
        self.val = val
        self.nxt = nxt
        self.sibling = sibling
