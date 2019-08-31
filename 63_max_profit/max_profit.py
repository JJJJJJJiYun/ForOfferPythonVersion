# -*- encoding: utf-8 -*-


def get_max_profit(array):
    if not array or len(array) < 2:
        return 0
    min_price = array[0]
    max_profit = array[1] - array[0]
    for i in range(1, len(array)):
        profit = array[i] - min_price
        if profit > max_profit:
            max_profit = profit
        if array[i] < min_price:
            min_price = array[i]
    return max_profit


if __name__ == '__main__':
    print get_max_profit([9, 11, 5, 7, 16, 1, 4, 2])
