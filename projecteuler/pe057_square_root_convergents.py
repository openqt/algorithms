# coding=utf-8
"""
Square root convergents
Problem 57

It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

    √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

    1 + 1/2 = 3/2 = 1.5
    1 + 1/(2 + 1/2) = 7/5 = 1.4
    1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
    1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than denominator?
"""
from __future__ import print_function


def square_two_fraction(count=-1):
    a, b = 3, 2
    while count != 0:
        yield a, b
        a, b = a + 2 * b, a + b
        count -= 1


def int_len(n):
    i = 0
    while n > 0:
        i += 1
        n //= 10
    return i


if __name__ == '__main__':
    count = 0
    for a, b in square_two_fraction(1000):
        count += 1 if int_len(a) > int_len(b) else 0
    print(count)  # 153
