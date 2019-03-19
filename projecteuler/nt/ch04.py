#!/usr/bin/env python
# coding=utf-8
from cProfile import run

from ch02 import GCD


def is_square(n):
    i = 1
    while n > 0:
        n -= i
        i += 2
    return n == 0


def fx(stop=-1):
    c = 1
    while stop != 0:
        c += 1
        for b in range(2, c + 1):
            for a in range(1, b + 1):
                if b ** 3 + a ** 3 == c ** 2:
                    stop -= 1
                    yield a, b, c


def Q4_2a(stop=-1):
    for n, i in enumerate(fx(stop), 1):
        print(n, i)


def _origin(a, b, c):
    if a == b:
        for i in (2, 3, 5, 7, 9, 11, 13):
            if i * i < a:
                if a % (i * i) == 0:
                    return i
            else:
                return 1
    else:
        n = GCD(a, b)
        if n > 1 and c % n == 0:
            n2 = int(n ** .5)
            if n2 * n2 == n:
                return n2 if c % n2 ** 3 == 0 else 1
    return 1


def Q4_2c(stop=-1):
    gen = fx()
    while stop != 0:
        seq = next(gen)
        n = _origin(*seq)
        if n > 1:
            print(n, seq)
            stop -= 1


if __name__ == '__main__':
    run("Q4_2a(10)")
    run("Q4_2c(5)")
    print(_origin(18, 18, 108))
