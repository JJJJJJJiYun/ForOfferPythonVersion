# -*- encoding: utf-8 -*-


class ListNode(object):
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

    def print_next_nodes(self):
        temp = self
        while temp:
            print temp.val
            temp = temp.nxt
