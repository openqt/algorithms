# coding=utf-8
"""
Spiral primes
Problem 58

Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed.

    37 36 35 34 33 32 31
    38 17 16 15 14 13 30
    39 18  5  4  3 12 29
    40 19  6  1  2 11 28
    41 20  7  8  9 10 27
    42 21 22 23 24 25 26
    43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the s
ide length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?
"""
from __future__ import print_function, division
from e0007_10001st_primes import is_prime

if __name__ == '__main__':
    n, step = 1, 2
    total, primes = 1, 0
    while True:
        for i in range(3):  # 2222, 4444, 6666, 8888, ...
            n += step
            total += 1
            primes += 1 if is_prime(n) else 0
        # the last one in each loop is not a prime, its n * n
        n += step
        total += 1
        step += 2

        if primes / total < 0.1:
            print(int(n ** .5))  # 26241
            break
