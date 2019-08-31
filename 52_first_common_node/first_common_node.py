# -*- encoding: utf-8 -*-
from structure.list_node import ListNode


def get_first_common_node(head1, head2):
    p = head1
    q = head2
    while p and q:
        p = p.nxt
        q = q.nxt
    longer_list_head = head1
    shorter_list_head = head2
    count = 0
    if p:
        while p:
            p = p.nxt
            count += 1
    if q:
        longer_list_head = head2
        shorter_list_head = head1
        while q:
            q = q.nxt
            count += 1
    for i in range(0, count):
        longer_list_head = longer_list_head.nxt
    while longer_list_head is not shorter_list_head:
        longer_list_head = longer_list_head.nxt
        shorter_list_head = shorter_list_head.nxt
    return longer_list_head


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node1.nxt = node2
    node2.nxt = node3
    node3.nxt = node4
    node4.nxt = node5
    node6.nxt = node7
    node7.nxt = node3
    print get_first_common_node(node1, node6).val
