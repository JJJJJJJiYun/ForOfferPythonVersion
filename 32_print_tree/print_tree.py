# -*- encoding: utf-8 -*-
from structure.tree_node import TreeNode


def print_binary_tree(root):
    if not root:
        return
    queue = [root]
    while queue:
        print queue[0].val,
        if queue[0].left:
            queue.append(queue[0].left)
        if queue[0].right:
            queue.append(queue[0].right)
        queue.pop(0)


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


def print_binary_tree_zigzag(root):
    if not root:
        return
    queues = {
        0: [],
        1: []
    }
    flag = 0
    next_flag = 1 - flag
    queues[flag].append(root)
    while queues[flag]:
        current_container = queues[flag]
        next_container = queues[next_flag]
        for i in range(0, len(current_container)):
            if flag:
                node = current_container.pop(0)
                print node.val,
                if node.right:
                    next_container.append(node.right)
                if node.left:
                    next_container.append(node.left)
            else:
                node = current_container.pop()
                print node.val,
                if node.left:
                    next_container.insert(0, node.left)
                if node.right:
                    next_container.insert(0, node.right)
        print "\n"
        flag = 1 - flag
        next_flag = 1 - flag


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    print_binary_tree(node1)
    print '\n----------'
    print_binary_tree_in_line(node1)
    print '\n----------'
    print_binary_tree_zigzag(node1)
