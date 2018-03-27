#!/usr/bin/env python
# coding=utf-8
"""
Digit factorial chains
Problem 74

The number 145 is well known for the property that the sum of the factorial of
its digits is equal to 145:

    1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of
numbers that link back to 169; it turns out that there are only three such
loops that exist:

    169 → 363601 → 1454 → 169
    871 → 45361 → 871
    872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get
stuck in a loop. For example,

    69 → 363600 → 1454 → 169 → 363601 (→ 1454)
    78 → 45360 → 871 → 45361 (→ 871)
    540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest
non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly
sixty non-repeating terms?
"""
from __future__ import print_function, division
from pe020_factorial_digit_sum import factorial
from pe030_digit_fifth_powers import sum_digit_by


def longest_factorial_chain(n, caches):
    """cached longest chain of numbers in each step

    :param n: the number
    :param caches:
    :return:
    """
    x = n  # save original number

    vals, val_set = [], set()  # vals for sequence, val_set for fast indexing
    while (n not in caches) and (n not in val_set):
        vals.append(n)
        val_set.add(n)
        n = sum_digit_by(n, factorial)

    n = len(vals) + caches.get(n, 0)  # anyway do the calculation
    for i in vals:
        caches[i] = n
        n -= 1

    return caches[x]


if __name__ == '__main__':
    caches = {}
    count = sum(1 for i in range(1000000) if
                longest_factorial_chain(i, caches) == 60)
    print('caches:', len(caches))
    print(count)  # 402
