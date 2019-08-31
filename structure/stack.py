# -*- encoding: utf-8 -*-


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.insert(0, val)

    def pop(self):
        self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0
