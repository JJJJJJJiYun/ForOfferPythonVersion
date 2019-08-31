# -*- encoding: utf-8 -*-


class MaxQueue(object):

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, val):
        self.queue1.append(val)
        max_val = self.queue2[len(self.queue2) - 1] \
            if self.queue2 and val < self.queue2[len(self.queue2) - 1] else val
        self.queue2.append(max_val)

    def pop(self):
        self.queue2.pop(0)
        return self.queue1.pop(0)

    def max(self):
        return self.queue2[0]


def get_max_num_in_sliding_window(array, k):
    if not array or len(array) < k:
        return None
    max_nums = []
    queue = []
    for i, num in enumerate(array):
        if queue and i - queue[0] >= k:
            queue.pop(0)
        while queue and num >= array[queue[len(queue) - 1]]:
            queue.pop()
        queue.append(i)
        if queue and i >= k - 1:
            max_nums.append(array[queue[0]])
    return max_nums


if __name__ == '__main__':
    print get_max_num_in_sliding_window([2, 3, 4, 2, 6, 2, 5, 1], 3)
