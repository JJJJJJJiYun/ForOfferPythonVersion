# -*- encoding: utf-8 -*-


class MinStack(object):

    def __init__(self):
        self.val_stack = []
        self.min_stack = []

    def push(self, val):
        self.val_stack.append(val)
        if len(self.min_stack) > 0:
            current_min = self.min_stack[len(self.min_stack) - 1]
            val = current_min if val > current_min else val
        self.min_stack.append(val)

    def pop(self):
        self.val_stack.pop()
        self.min_stack.pop()

    def min(self):
        return self.min_stack[len(self.min_stack) - 1]


if __name__ == '__main__':
    stack = MinStack()
    stack.push(1)
    stack.push(2)
    print stack.min()
    stack.push(0)
    print stack.min()
    stack.pop()
    print stack.min()
