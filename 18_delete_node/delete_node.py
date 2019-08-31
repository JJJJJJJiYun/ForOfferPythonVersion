# -*- encoding: utf-8 -*-

from structure.list_node import ListNode


def delete_node(head, node):
    if not head or not node or head is node:
        return None
    if not node.nxt:
        temp = head
        while temp.nxt.nxt:
            temp = temp.nxt
        temp.nxt = None
    else:
        node.val = node.nxt.val
        node.nxt = node.nxt.nxt
    return head


def delete_duplicate_node(head):
    if not head:
        return None
    dummy = ListNode(head.val - 1)
    dummy.nxt = head
    former = dummy
    latter = head
    while latter:
        if latter.nxt and latter.val == latter.nxt.val:
            while latter.nxt and latter.val == latter.nxt.val:
                latter = latter.nxt
            former.nxt = latter.nxt
            latter = latter.nxt
        else:
            former = former.nxt
            latter = latter.nxt
    return dummy.nxt


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(4)
    node6 = ListNode(6)
    node1.nxt = node2
    node2.nxt = node3
    node3.nxt = node4
    node4.nxt = node5
    node5.nxt = node6
    result = delete_node(node1, node3)
    if result:
        result.print_next_nodes()
    print "----------"
    result = delete_duplicate_node(node1)
    if result:
        result.print_next_nodes()
