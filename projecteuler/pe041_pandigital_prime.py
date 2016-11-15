# coding=utf-8
"""
Pandigital prime
Problem 41

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""
from __future__ import print_function
from pe007_10001st_primes import is_prime
from pe024_lexicographic_permutations import permutations
from pe032_pandigital_products import int_seq


if __name__ == '__main__':
    val = 0
    for i in range(9, 0, -1):
        if sum(range(i + 1)) % 3 == 0:  # 可以被3整除不是质数
            continue

        for i in permutations(range(1, i + 1)):
            n = int_seq(i)
            if is_prime(n):
                val = max(val, n)

        if val > 0:
            break
    print(val)  # 7652413
