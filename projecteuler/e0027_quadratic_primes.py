# coding=utf-8
"""
Quadratic primes
Problem 27

Euler discovered the remarkable quadratic formula:

    n^2+n+41
It turns out that the formula will produce 40 primes for the consecutive
integer values 0≤n≤39. However, when n=40,40^2+40+41=40(40+1)+41 is
divisible by 41, and certainly when n=41,41^2+41+41 is clearly divisible by 41.

The incredible formula n^2−79n+1601 was discovered, which produces 80 primes
for the consecutive values 0≤n≤790≤n≤79. The product of the coefficients,
−79 and 1601, is −126479.

Considering quadratics of the form:

    n^2+an+b, where |a|<1000| and |b|≤1000

    where |n| is the modulus/absolute value of n
    e.g. |11|=11=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n=0.
"""
from __future__ import print_function
from e0003_largest_prime_factor import prime_sieve
from e0007_10001st_primes import is_prime


def prime_quadratic_formula(a, b):
    n = 0
    while True:
        yield n ** 2 + a * n + b
        n += 1


def _len_primes(a, b):
    for n, i in enumerate(prime_quadratic_formula(a, b)):
        if not is_prime(i):
            return n


if __name__ == '__main__':
    max_val = max_len = 0
    for a in range(-999, 1000):
        for b in prime_sieve(1000):  # b must be prime for n = 0
            for i in (b, -b):
                _len = _len_primes(a, i)
                if max_len < _len:
                    max_len = _len
                    max_val = (a, i)

    print(max_val, max_len)
    print(max_val[0] * max_val[1])  # -59231

