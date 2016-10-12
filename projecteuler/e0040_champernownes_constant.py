# coding=utf-8
"""
Champernowne's constant
Problem 40

An irrational decimal fraction is created by concatenating the positive
integers:

    0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
from __future__ import print_function


if __name__ == '__main__':
    d = ''
    for i in range(1000000):
        d += str(i)

    total = 1
    mul = 1
    for i in range(7):
        total *= int(d[mul])
        mul *= 10
    print(total)
