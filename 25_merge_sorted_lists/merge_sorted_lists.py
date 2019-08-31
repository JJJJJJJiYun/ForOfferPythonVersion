# -*- encoding: utf-8 -*-
from structure.list_node import ListNode


def merge_sorted_lists(head1, head2):
    if not head1 and not head2:
        return None
    if (head1 and not head2) or (head2 and not head1):
        return head1 if head1 else head2
    dummy = ListNode(0)
    p = head1
    q = head2
    last = dummy
    while p and q:
        if p.val < q.val:
            last.nxt = p
            last = p
            p = p.nxt
        else:
            last.nxt = q
            last = q
            q = q.nxt
    left = p if p else q
    while left:
        last.nxt = left
        last = left
        left = left.nxt
    return dummy.nxt


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node1.nxt = node2
    node2.nxt = node3
    node4.nxt = node5
    node5.nxt = node6
    head = merge_sorted_lists(node1, node4)
    if head:
        while head:
            print head.val
            head = head.nxt
