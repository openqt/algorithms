#!/usr/bin/env python
# coding=utf-8
"""
Totient permutation
Problem 70

Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of positive numbers less than or equal to n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than
nine and relatively prime to nine, φ(9)=6.

The number 1 is considered to be relatively prime to every positive number,
so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation
of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the
ratio n/φ(n) produces a minimum.
"""
from __future__ import print_function, division
from utils import prime_sieve
from pe049_prime_permutations import seq_int
from pe069_totient_maximum import totient


def index_by_ceil(seq, ceil):
    """return index below ceil

    :param seq: list
    :param ceil: the maximum value
    :return: index
    """
    n = 0
    for i in seq:
        if i > ceil:
            break
        n += 1
    return n


if __name__ == '__main__':
    CEIL = 10000000
    caches = [i for i in prime_sieve(CEIL)]

    pos = index_by_ceil(caches, CEIL ** .5)
    val = (CEIL, CEIL)

    for n, i in enumerate(caches[:pos]):
        end = index_by_ceil(caches, CEIL / i)
        for j in caches[n + 1:end]:
            n = i * j
            phi = totient(n, i, j)
            if sorted(seq_int(phi)) == sorted(seq_int(n)):
                val = min(val, (n / phi, n))
    print(val)  # 8319823
