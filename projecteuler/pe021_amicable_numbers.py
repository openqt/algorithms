# coding=utf-8
"""
Amicable numbers
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from __future__ import print_function
from pe012_highly_divisible_triangular_number import prime_factors


def proper_divisors(n):
    """proper divisor sequence

    :param n: number
    :return: proper divisor sequence
    """
    if n <= 1:
        return

    yield 1

    step = n % 2 + 1  # odd numbers cannot have even numbers as divisors.
    # (The converse is not true: even numbers can have odd divisors).
    i = step + 1
    # when we found one of the two in fact we know the other.
    while i < n ** .5:
        if n % i == 0:
            yield i
            yield n / i

        i += step

    if i * i == n:  # special care is perfect square.
        yield i


def sum_proper_divisors(n):
    factors = prime_factors(n)
    total = 1
    for x, y in factors.items():
        total *= (x ** (y + 1) - 1) / (x - 1)
    return total - n


def amicable_number(stop=-1):
    """amicable number sequence

    :param stop: the maximum number
    :return: amicable number sequence
    """
    caches = {}

    a = 1
    while True:
        a += 1
        if 0 < stop < a:
            break

        b = caches[a] if a in caches else caches.setdefault(
            a, sum_proper_divisors(a))  # d(a) = b

        if a < b:  # a != b and make sure a is lower
            aa = caches[b] if b in caches else caches.setdefault(
                b, sum_proper_divisors(b))  # d(b) = a

            if aa == a:
                yield a, b


if __name__ == '__main__':
    print(sum(a + b for a, b in amicable_number(10000)))  # 31626
