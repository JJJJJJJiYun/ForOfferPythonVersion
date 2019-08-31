# -*- encoding: utf-8 -*-
from structure.heap import MaxHeap, MinHeap


def find_median(array):
    max_heap = MaxHeap()
    min_heap = MinHeap()
    for num in array:
        # 插入第偶数个数时，插入最小堆
        if (max_heap.size() + min_heap.size()) & 1 == 0:
            if max_heap.size() > 0 and num < max_heap.peek():
                max_heap.push(num)
                num = max_heap.pop()
            min_heap.push(num)
        else:
            if min_heap.size() > 0 and num > min_heap.peek():
                min_heap.push(num)
                num = min_heap.pop()
            max_heap.push(num)
    return (max_heap.peek() + min_heap.peek()) / 2.0 if \
        (max_heap.size() + min_heap.size()) & 1 == 0 else \
        min_heap.peek()


if __name__ == '__main__':
    print find_median([2, 4, 3, 1, 5, 7, 6, 8])
