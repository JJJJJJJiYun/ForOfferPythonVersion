# -*- encoding: utf-8 -*-
from structure.tree_node import print_binary_tree_in_line, TreeNode


class Solution(object):
    def __init__(self):
        self.index = 0

    def serialize_binary_tree(self, root):
        if not root:
            return "$ "
        return str(root.val) + " " + self.serialize_binary_tree(
            root.left) + self.serialize_binary_tree(root.right)

    def deserialize_binary_tree(self, sequence):
        if sequence[self.index] != '$':
            root = TreeNode(int(sequence[self.index]))
            self.index += 2
            root.left = self.deserialize_binary_tree(sequence)
            root.right = self.deserialize_binary_tree(sequence)
            return root
        self.index += 2
        return None


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
    solution = Solution()
    sequence = solution.serialize_binary_tree(node1)
    root = solution.deserialize_binary_tree(sequence)
    print_binary_tree_in_line(root)
