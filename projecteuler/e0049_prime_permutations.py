# coding=utf-8
"""
Prime permutations
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways:
    (i) each of the three terms are prime, and,
    (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""
from __future__ import print_function
from e0003_largest_prime_factor import prime_sieve


def seq_int(n):
    """int to sequence

    :param n: number
    :return: digit sequence
    """
    seq = []
    while n > 0:
        seq.append(n % 10)
        n /= 10
    seq.reverse()
    return seq


def longest_ap(seq):
    """calculate the longest arithmetic progression from given sequence

    :param seq: sequence
    :return: the longest arithmetic progression
    """
    val = (0, 0, 0)  # first number, step, length
    seq = sorted(seq)
    for n, i in enumerate(seq):
        for j in seq[:n]:
            n = 0
            while 2 * i - j in seq:
                n += 1
                i, j = 2 * i - j, i

            if n > val[0]:
                val = (j - (i - j) * n, i - j, n + 2)

    return [val[0] + val[1] * i for i in range(val[2])]


if __name__ == '__main__':
    caches = {}
    for i in prime_sieve(10000):
        if i > 1000:
            seq = tuple(sorted(seq_int(i)))
            caches.setdefault(seq, []).append(i)  # 按排序分组，默认即升序

    for v in caches.values():
        if len(v) >= 3:  # 需要满足最少有3个质数
            ap = longest_ap(v)
            if ap:
                print(v, '=>', ap)  # 296962999629
