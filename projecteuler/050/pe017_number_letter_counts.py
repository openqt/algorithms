#!/usr/bin/env python
# coding=utf-8
"""
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""
from __future__ import print_function

_NUMBERS = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    # 100: 'hundred',
    # 1000: 'thousand',
}


def get_digit(n, digit=1, keep=True):
    n = (n % (10 ** digit) / 10 ** (digit - 1))
    if keep:
        n *= 10 ** (digit - 1)
    return n


def digit_1(n):
    n %= 10
    return len(_NUMBERS[n])


def digit_10(n):
    n %= 100
    if n in _NUMBERS:
        return len(_NUMBERS[n])
    return len(_NUMBERS[get_digit(n, 2)]) + digit_1(n)


def digit_100(n):
    n %= 1000
    high = len(_NUMBERS[get_digit(n, 3, False)])
    low = digit_10(n)

    if high == 0:
        return low

    high += low + len('hundred')
    if low > 0:
        high += len('and')

    return high


def digit_1000(n):
    n %= 10000
    high = len(_NUMBERS[get_digit(n, 4, False)])
    low = digit_100(n)

    if high == 0:
        return low

    return high + len('thousand') + low


if __name__ == '__main__':
    print(digit_1000(201))  # two hundred and one = 16
    print(digit_1000(342))  # three hundred and forty-two = 23
    print(digit_1000(115))  # one hundred and fifteen = 20
    print(digit_1000(1000))  # one thousand = 11
    print(sum(digit_1000(i) for i in range(1, 6)))  # 19

    print(sum(digit_1000(i) for i in range(1, 1001)))  # 21124
