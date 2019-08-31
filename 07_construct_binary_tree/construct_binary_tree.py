# -*- encoding: utf-8 -*-

from structure.tree_node import TreeNode


def construct_binary_tree(pre_order, in_order):
    return construct_helper(pre_order, in_order, 0, len(pre_order) - 1, 0,
                            len(in_order) - 1)


def construct_helper(pre_order, in_order, pre_start, pre_end, in_start, in_end):
    if pre_start > pre_end:
        return
    index = -1
    for (i, num) in enumerate(in_order):
        if num == pre_order[pre_start]:
            index = i
            break
    if index == -1:
        raise RuntimeError(u"错误的输入")
    root = TreeNode(pre_order[index])
    left_length = index - in_start
    root.left = construct_helper(pre_order, in_order, pre_start + 1,
                                 pre_start + left_length, in_start, index - 1)
    root.right = construct_helper(pre_order, in_order,
                                  pre_start + left_length + 1, pre_end,
                                  index + 1, in_end)
    return root
