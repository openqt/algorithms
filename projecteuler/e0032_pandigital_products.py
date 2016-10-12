# coding=utf-8
"""
Pandigital products
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""
from __future__ import print_function
from e0024_lexicographic_permutations import permutations


def int_seq(seq):
    """convert sequence to int

    :param seq: sequence
    :return: int
    """
    n = 0
    for i in seq:
        n = n * 10 + int(i)
    return n
    # return int(''.join(seq))  # not for special cases
    # return reduce(lambda x, y: int(x) * 10 + int(y), seq)  # buggy


def _pandigital(seq):
    """
        a × bcde = fghi
        ab × cde = fghi
    :param i:
    :return:
    """
    for i in permutations(seq):
        val = int_seq(i[5:])
        if int_seq(i[:1]) * int_seq(i[1:5]) == val or \
           int_seq(i[:2]) * int_seq(i[2:5]) == val:
            yield val


if __name__ == '__main__':
    total = set(i for i in _pandigital('123456789'))
    print(total)
    print(sum(total))  # 45228
