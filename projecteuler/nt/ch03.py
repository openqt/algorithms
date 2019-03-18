#!/usr/bin/env python
# coding=utf-8
from cProfile import run


def Q3_1(u=10, v=10):
    def _calc():
        for i in range(1, u):
            for j in range(1, i):
                yield i * i - j * j, 2 * i * j, i * i + j * j, (i, j)

    for i in _calc():
        print(i)


if __name__ == '__main__':
    run("Q3_1()")
