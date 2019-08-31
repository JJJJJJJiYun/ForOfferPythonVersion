# -*- encoding: utf-8 -*-
from structure.list_node import ListNode


def find_entry_of_loop(head):
    p = q = find_node_in_loop(head)
    if not p:
        return None
    count = 1
    p = p.nxt
    while p is not q:
        count += 1
        p = p.nxt
    p = head
    q = head
    for i in range(0, count):
        p = p.nxt
    while p is not q:
        p = p.nxt
        q = q.nxt
    return p


def find_node_in_loop(head):
    if not head:
        return None
    p = head.nxt
    if not p:
        return None
    q = p.nxt
    if not q:
        return None
    while p and q and p is not q:
        p = p.nxt
        q = q.nxt
        if q:
            q = q.nxt
    return p


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node1.nxt = node2
    node2.nxt = node3
    node3.nxt = node4
    node4.nxt = node5
    node5.nxt = node6
    node6.nxt = node3
    result = find_entry_of_loop(node1)
    if result:
        print result.val
