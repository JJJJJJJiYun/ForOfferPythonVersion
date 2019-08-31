# -*- encoding: utf-8 -*-
from structure.list_node import ListNode


def reverse_list(head):
    if not head or not head.nxt:
        return head
    dummy = ListNode(-1, head)
    p, q, r = dummy, head, head.nxt
    while True:
        q.nxt = p
        if not r:
            break
        p = q
        q = r
        r = r.nxt
    head.nxt = None
    return q


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
    result = reverse_list(node1)
    while result:
        print result.val
        result = result.nxt
