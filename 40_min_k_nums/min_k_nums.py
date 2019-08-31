# -*- encoding: utf-8 -*-
import heapq

from sort.quick_sort import get_index


def min_k_nums(array, k):
    start = 0
    end = len(array) - 1
    while start <= end:
        index = get_index(array, start, end)
        if index < k:
            start = index + 1
        elif index > k:
            end = index - 1
        else:
            for i in range(0, k):
                print array[i],
            break


def min_k_nums_with_heap(array, k):
    heap = []
    for num in array:
        num = -num
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappushpop(heap, num)
    for num in heap:
        print -num,


if __name__ == '__main__':
    min_k_nums([4, 5, 1, 6, 2, 7, 3, 8], 4)
    min_k_nums_with_heap([4, 5, 1, 6, 2, 7, 3, 8], 4)
