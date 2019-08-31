# -*- encoding: utf-8 -*-
from structure.complex_list_node import ComplexListNode


def copy_complex_list(head):
    if not head:
        return None
    p = head
    while p:
        q = ComplexListNode(p.val)
        q.nxt = p.nxt
        p.nxt = q
        p = q.nxt
    p = head
    q = p.nxt
    while p:
        if p.sibling:
            q.sibling = p.sibling.nxt
        p = q.nxt
        if p:
            q = p.nxt
    p = head
    q = p.nxt
    result = p.nxt
    while p:
        p.nxt = q.nxt
        if q.nxt:
            q.nxt = q.nxt.nxt
        p = p.nxt
        q = q.nxt
    return result


if __name__ == '__main__':
    node1 = ComplexListNode(1)
    node2 = ComplexListNode(2)
    node3 = ComplexListNode(3)
    node4 = ComplexListNode(4)
    node5 = ComplexListNode(5)
    node6 = ComplexListNode(6)
    node1.nxt = node2
    node2.nxt = node3
    node3.nxt = node4
    node4.nxt = node5
    node1.sibling = node3
    node2.sibling = node5
    node4.sibling = node2
    result = copy_complex_list(node1)
    while result:
        print result.val
        result = result.nxt
