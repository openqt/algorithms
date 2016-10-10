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


def combations_by(number, choices):
    if len(choices) <= 1:
        return 1

    if number < 0:
        return 0

    return sum(combations_by(number - i, choices[:n+1])
               for n, i in enumerate(choices))


if __name__ == '__main__':
    print(combations_by(200, [1, 2, 5, 10, 20, 50, 100, 200]))  # 73682
