# -*- encoding: utf-8 -*-


def find_next_node(root):
    if not root:
        return None
    # 如果有右子节点，那下一个是右子节点的最左子节点
    if root.right:
        temp = root.right
        while temp.left is not None:
            temp = temp.left
        return temp
    # 如果没有右子节点，且是父节点的左子节点，那下一个节点为父节点
    if root == root.father.left:
        return root.father
    temp = root.father
    while temp.father and temp == temp.father.right:
        temp = temp.father
    return temp.father
