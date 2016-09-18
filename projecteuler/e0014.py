# coding=utf-8
"""
Longest Collatz sequence
Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms.
Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def collatz(n):
    """
    generating Collatz sequence by starting number
    :param n: start number
    :return: Collatz sequence
    """
    while n > 1:
        yield n

        if n & 1 == 0:
            n >>= 1
        else:
            n = 3 * n + 1
    yield 1


def _len_collatz(n, cache):
    """
    length of generator
    :param gen: generator
    :return: length
    """
    length = 0
    for i in collatz(n):
        if i in cache:
            cache[n] = length + cache[i]
            break
        else:
            length += 1
    else:
        cache[n] = length
    return cache[n]


if __name__ == '__main__':
    val = 0
    num = 0
    cache = {}
    for i in range(1, 1000000, 2):
        count = _len_collatz(i, cache)
        if val < count:
            val = count
            num = i

    print(num, val)  # (837799, 525)
