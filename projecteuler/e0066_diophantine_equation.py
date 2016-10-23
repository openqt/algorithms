# coding=utf-8
"""
Diophantine equation
Problem 66

Consider quadratic Diophantine equations of the form:

    x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is
square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

    32 – 2×22 = 1
    22 – 3×12 = 1
    92 – 5×42 = 1
    52 – 6×22 = 1
    82 – 7×32 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is
obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value
of x is obtained.
"""
from __future__ import print_function
from e0046_goldbachs_other_conjecture import sqrt_is_int


def diophantine(D, y=1):
    if sqrt_is_int(D):
        return None

    while not sqrt_is_int(1 + D * y ** 2):
        y += 1
    return int((1 + D * y ** 2) ** .5)


if __name__ == '__main__':
    # print(min(diophantine(D) for D in range(2, 1001)))
    for D in range(62, 1001):
        print('>', D, diophantine(D))
