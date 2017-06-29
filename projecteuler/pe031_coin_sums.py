# coding=utf-8
"""
Coin sums
Problem 31

In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""
from __future__ import print_function


# def different_ways(number, choices):
#     """
#
#     :param number: total
#     :param choices: list of choices
#     :return:
#     """
#     if len(choices) <= 1:
#         return 1
#
#     if number < 0:
#         return 0
#
#     return sum(different_ways(number - i, choices[:n + 1])
#                for n, i in enumerate(choices))


def different_ways(n, seq, all=False):
    """return the number of different combination ways by n,k

    refer to: http://www.mathblog.dk/project-euler-31-combinations-english-currency-denominations/

    :param n: total
    :param seq: choices
    :param all: return intermediate results
    :return: how many different ways
    """
    ways = [0] * (n + 1)
    ways[0] = 1
    for val in seq:
        for i in range(val, n + 1):
            ways[i] += ways[i - val]
    return ways if all else ways[n]


if __name__ == '__main__':
    print(different_ways(200, [1, 2, 5, 10, 20, 50, 100, 200]))  # 73682
