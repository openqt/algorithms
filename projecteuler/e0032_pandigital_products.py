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
from e0024_lexicographic_permutations import next_permutation


def _int(seq):
    """convert sequence to int

    :param seq: sequence
    :return: int
    """
    return reduce(lambda x, y: x * 10 + int(y), seq)


def _pandigital(seq):
    """
        a × bcde = fghi
        ab × cde = fghi
    :param seq:
    :return:
    """
    stop = seq[:]
    while next_permutation(seq) != stop:
        val = _int(seq[5:])
        if _int(seq[:1]) * _int(seq[1:5]) == val or \
           _int(seq[:2]) * _int(seq[2:5]) == val:
            yield val


if __name__ == '__main__':
    total = set(i for i in _pandigital([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(total)
    print(sum(total))  # 45228
