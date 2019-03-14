#!/usr/bin/env python
# coding=utf-8
from cProfile import run


def GCD(m, n):
    while n > 0:
        m, n = n, m % n
    return m


def PPT(t=10, s=10):
    for i in range(1, t, 2):
        for j in range(i + 2, s, 2):
            if GCD(j, i) == 1:
                yield j * i, (j * j - i * i) // 2, (j * j + i * i) // 2, (j, i)


def Q2_4(t=100, s=100):
    data = {}
    for i in PPT(t, s):
        data.setdefault(i[2], []).append(i)

    n = 0
    for k in data:
        if len(data[k]) > 1:
            n += 1
            print(">", n, data[k])


def Q2_6(stop=-1):
    n = 0
    for i in PPT(100, 100):
        if i[2] - i[0] == 2:
            n += 1
            print(">", n, i)
            if n == stop:
                return


def Q2_7():
    for i in PPT(100, 100):
        print(">", i, 2 * (i[2] - i[0]))


def Q2_8():
    from fractions import Fraction
    for i in PPT(20, 20):
        print(i)

    for n in range(2, 10):
        print(Fraction(1, n) + Fraction(1, n + 2))


run("Q2_4()")
run("Q2_6()")
run("Q2_7()")
Q2_8()
