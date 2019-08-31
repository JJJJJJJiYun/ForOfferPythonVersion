# -*- encoding: utf-8 -*-

from structure.list_node import ListNode


def find_kth_node_in_list(head, k):
    if not head:
        return None
    count = 1
    temp = head
    while temp.nxt and count < k:
        count += 1
        temp = temp.nxt
    if count < k:
        return None
    while temp.nxt:
        head = head.nxt
        temp = temp.nxt
    return head


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.nxt = node2
    node2.nxt = node3
    node3.nxt = node4
    result = find_kth_node_in_list(node5, 1)
    if result:
        print result.val
