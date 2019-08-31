# -*- encoding: utf-8 -*-
from structure.tree_node import TreeNode


class Solution(object):

    def __init__(self):
        self.count = 0
        self.result = None

    def find_kth_node_in_bst(self, root, k):
        if not root:
            return
        self.find_kth_node_in_bst(root.left, k)
        self.count += 1
        if self.count == k:
            self.result = root
        self.find_kth_node_in_bst(root.right, k)


if __name__ == '__main__':
    node1 = TreeNode(5)
    node2 = TreeNode(3)
    node3 = TreeNode(7)
    node4 = TreeNode(2)
    node5 = TreeNode(4)
    node6 = TreeNode(6)
    node7 = TreeNode(8)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    solution = Solution()
    solution.find_kth_node_in_bst(node1, 7)
    print solution.result.val
