#!/usr/bin/env python
# coding=utf-8
"""
Digit cancelling fractions
Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""
from __future__ import print_function
from __future__ import division


def non_trivial_cancelling():
    for i in range(11, 100):  # 分母
        for j in range(11, i):  # 分子
            ia, ib = divmod(i, 10)
            ja, jb = divmod(j, 10)

            if ib == 0 or jb == 0:  # 10的倍数
                continue

            div = j / i
            if (ia == ja and jb / ib == div) or \
                    (ia == jb and ja / ib == div) or \
                    (ib == ja and jb / ia == div) or \
                    (ib == jb and ja / ia == div):
                yield j, i


if __name__ == '__main__':
    val = 1
    for i, j in non_trivial_cancelling():
        print('{} / {} = {}'.format(i, j, i / j))
        val *= j / i  # 无需化简，小数乘积的倒数即是
    print(val)  # 100
