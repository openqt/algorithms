#!/usr/bin/env python
# coding=utf-8
from cProfile import run


def square_number(stop=-1):
    n = 1
    while n != stop:
        yield n * n
        n += 1


def triangular_number(stop=-1):
    prev, n = 0, 1
    while n != stop:
        yield n + prev
        prev += n
        n += 1


def Q1_1(loop=3):
    print(list(square_number(20)))
    print(list(triangular_number(20)))

    sng, tng = square_number(), triangular_number()
    sn, tn = next(sng), next(tng)
    while loop != 0:
        if sn == tn:
            print(">", sn)
            loop -= 1
            sn, tn = next(sng), next(tng)
        elif sn > tn:
            tn = next(tng)
        else:
            sn = next(sng)


run("Q1_1(4)")
