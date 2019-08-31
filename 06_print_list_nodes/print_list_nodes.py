# -*- encoding: utf-8 -*-
from structure.list_node import ListNode


def print_list_nodes(head):
    stack = []
    while head is not None:
        stack.insert(0, head)
        head = head.nxt
    for node in stack:
        print node.val


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.nxt = node2
    node2.nxt = node3
    node3.nxt = node4
    print_list_nodes(node1)
