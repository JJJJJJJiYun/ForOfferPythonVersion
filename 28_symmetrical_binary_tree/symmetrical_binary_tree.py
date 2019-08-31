# -*- encoding: utf-8 -*-
from structure.tree_node import TreeNode


def is_symmetrical_binary_tree(root):
    pre_order = []
    right_pre_order = []
    pre_order_traversal(root, pre_order)
    right_pre_order_traversal(root, right_pre_order)
    for i, value in enumerate(pre_order):
        if value != right_pre_order[i]:
            return False
    return True


def pre_order_traversal(root, pre_order):
    if not root:
        pre_order.append(None)
        return
    pre_order.append(root.val)
    pre_order_traversal(root.left, pre_order)
    pre_order_traversal(root.right, pre_order)


def right_pre_order_traversal(root, pre_order):
    if not root:
        pre_order.append(None)
        return
    pre_order.append(root.val)
    right_pre_order_traversal(root.right, pre_order)
    right_pre_order_traversal(root.left, pre_order)


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(5)
    node7 = TreeNode(4)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    print is_symmetrical_binary_tree(node1)
