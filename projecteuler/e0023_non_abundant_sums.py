# coding=utf-8
"""
Non-abundant sums
Problem 23

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though
it is known that the greatest number that cannot be expressed as the sum of two
abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""
from __future__ import print_function
from e0021_amicable_numbers import sum_proper_divisors


def perfect_number(stop=-1):
    n = 5
    while True:
        n += 1
        if 0 < stop <= n:
            break

        if sum_proper_divisors(n) == n:
            yield n


def abundant_number(stop=-1):
    n = 11
    while True:
        n += 1
        if 0 < stop <= n:
            break

        if sum_proper_divisors(n) > n:
            yield n


if __name__ == '__main__':
    caches = set()
    caches_sorted = []
    for i in abundant_number(28123 + 1):
        caches.add(i)
        caches_sorted.append(i)

    # as 12 is the smallest abundant number, the smallest number that can be
    # written as the sum of two abundant numbers is 24
    total = sum(range(24))
    for i in range(25, 28123 + 1):
        can = False
        for j in caches_sorted:
            if j >= i:
                break

            if (i - j) in caches:
                can = True
                break

        if not can:
            total += i

    print(total)  # 4179871
