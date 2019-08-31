# -*- encoding: utf-8 -*-
from structure.tree_node import TreeNode


def print_path_of_n(root, n):
    if not root:
        return
    helper(root, n, 0, [])


def helper(root, n, val, nodes):
    val += root.val
    nodes.append(root)
    if not root.left and not root.right:
        if val == n:
            for node in nodes:
                print node.val,
            print "\n"
        nodes.pop()
        return
    if root.left:
        helper(root.left, n, val, nodes)
    if root.right:
        helper(root.right, n, val, nodes)
    nodes.pop()


if __name__ == '__main__':
    node1 = TreeNode(10)
    node2 = TreeNode(5)
    node3 = TreeNode(12)
    node4 = TreeNode(4)
    node5 = TreeNode(7)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    print_path_of_n(node1, 22)
