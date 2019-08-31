# -*- encoding: utf-8 -*-
from structure.tree_node import TreeNode


def is_substructure_of_tree(root1, root2):
    if not root1 or not root2:
        return False
    if helper(root1, root2):
        return True
    if is_substructure_of_tree(root1.left, root2):
        return True
    if is_substructure_of_tree(root1.right, root2):
        return True
    return False


def helper(root1, root2):
    if not root2:
        return True
    if not root1 or root1.val != root2.val:
        return False
    return helper(root1.left, root2.left) and helper(root1.right, root2.right)


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
    node8 = TreeNode(2)
    node9 = TreeNode(4)
    node10 = TreeNode(5)
    node8.left = node9
    node8.right = node10
    print is_substructure_of_tree(node1, node8)
