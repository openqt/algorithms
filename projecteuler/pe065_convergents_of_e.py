# coding=utf-8
"""
Convergents of e
Problem 65

The square root of 2 can be written as an infinite continued fraction.

    √2 = 1 +1
            2 +1
               2 +1
                  2 +1
                     2 + ...

The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates
that 2 repeats ad infinitum. In a similar way, √23 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions for
square roots provide the best rational approximations. Let us consider the
convergents for √2.

    1 + 1 = 3/2
        2

    1 + 1 = 7/5
        2 + 1
            2

    1 + 1 = 17/12
        2 + 1
            2 + 1
                2

    1 + 1 = 41/29
        2 + 1
            2 + 1
                2 + 1
                    2

Hence the sequence of the first ten convergents for √2 are:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
What is most surprising is that the important mathematical constant,

    e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

    2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the
continued fraction for e.
"""
from __future__ import print_function
from pe016_power_digit_sum import sum_digit


def converget_cf(cf, count=-1):
    """get value from continued fraction

    :param cf: continued fraction expression
    :param count:
    :return:
    """
    if len(cf) < 2:
        return

    p, q = [1, cf[0]], [0, 1]
    while True:
        for i in cf[1:]:
            if count == 0:
                return
            count -= 1

            yield p[1], q[1]
            p[0], p[1] = p[1], i * p[1] + p[0]
            q[0], q[1] = q[1], i * q[1] + q[0]


def e_cf(count):
    """e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...]

    :param count: the length of continued fraction
    :return:
    """
    n, e = 2, [2, ]
    while len(e) < count + 1:
        e += [1, n, 1]
        n += 2
    return e[:count + 1]


if __name__ == '__main__':
    for i in converget_cf(e_cf(100), 100):
        pass
    print(sum_digit(i[0]))  # 272
