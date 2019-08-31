# -*- encoding: utf-8 -*-
from structure.stack import Stack


class QueueWithTwoStack(object):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def append_tail(self, val):
        self.stack1.push(val)

    def delete_head(self):
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
