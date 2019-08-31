# -*- encoding: utf-8 -*-
from structure.tree_node import TreeNode


def get_mirror_of_tree(root):
    if not root:
        return
    if not root.left and not root.right:
        return
    temp = root.left
    root.left = root.right
    root.right = temp
    if root.left:
        get_mirror_of_tree(root.left)
    if root.right:
        get_mirror_of_tree(root.right)


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
    get_mirror_of_tree(node1)
