# coding=utf-8
"""
Prime summations
Problem 77

It is possible to write ten as the sum of primes in exactly five different ways:

    7 + 3
    5 + 5
    5 + 3 + 2
    3 + 3 + 2 + 2
    2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five
thousand different ways?
"""
from __future__ import print_function
from pe003_largest_prime_factor import prime_sieve
from pe031_coin_sums import different_ways


if __name__  == '__main__':
    primes = list(prime_sieve(1000))
    for n in range(10, 1000):
        if different_ways(n, primes) > 5000:
            print(n, different_ways(n, primes))  # 71, 5007
            break
