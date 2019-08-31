# -*- encoding: utf-8 -*-
from structure.tree_node import TreeNode


class Solution(object):
    def __init__(self):
        self.pre = None

    def convert_binary_search_tree(self, root):
        if not root:
            return None
        self.convert_helper(root)
        while root.left:
            root = root.left
        return root

    def convert_helper(self, root):
        if root.left:
            self.convert_helper(root.left)
        root.left = self.pre
        if self.pre:
            self.pre.right = root
        self.pre = root
        if root.right:
            self.convert_helper(root.right)


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
    result = Solution().convert_binary_search_tree(node1)
    while result:
        print result.val
        result = result.right
