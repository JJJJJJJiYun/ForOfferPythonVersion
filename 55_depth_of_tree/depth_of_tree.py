# -*- encoding: utf-8 -*-
from structure.tree_node import TreeNode


def get_depth_of_tree(root):
    if not root:
        return 0
    left = get_depth_of_tree(root.left)
    right = get_depth_of_tree(root.right)
    return left + 1 if left > right else right + 1


def is_balanced_tree(root):
    if not root:
        return True, 0
    left, left_depth = is_balanced_tree(root.left)
    right, right_depth = is_balanced_tree(root.right)
    return left and right and abs(
        left_depth - right_depth) <= 1, \
           left_depth + 1 if left_depth > right_depth else right_depth + 1


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
    print get_depth_of_tree(node1)
    print is_balanced_tree(node1)
