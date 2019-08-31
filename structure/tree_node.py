# -*- encoding: utf-8 -*-


def print_binary_tree_in_line(root):
    if not root:
        return
    queue = [root]
    current_num = 1
    next_num = 0
    while current_num > 0:
        for i in range(0, current_num):
            print queue[0].val,
            if queue[0].left:
                queue.append(queue[0].left)
                next_num += 1
            if queue[0].right:
                queue.append(queue[0].right)
                next_num += 1
            queue.pop(0)
        print "\n"
        current_num = next_num
        next_num = 0


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
