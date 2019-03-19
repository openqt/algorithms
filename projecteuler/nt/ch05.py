#!/usr/bin/env python
# coding=utf-8

from ch02 import GCD


def LCM(a, b):
    return a * b // GCD(a, b)


def n3_plus_1(n, stop=-1):
    while stop != 0:
        yield n
        stop -= 1

        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1


def len_3plus1(n):
    cache = set()
    for i in n3_plus_1(n, 1000):
        if i in cache:
            return len(cache)
        cache.add(i)
    return -1


def Q5_1():
    print(GCD(12345, 67890))
    print(GCD(54321, 9876))


def Q5_2():
    print(GCD(0, 0))


def Q5_4():
    print(LCM(3, 7), LCM(12, 66))
    print(LCM(8, 12), LCM(20, 30), LCM(51, 68), LCM(23, 18))


def Q5_5():
    print([i for i in n3_plus_1(5, 12)])
    print([i for i in n3_plus_1(7, 20)])


def Q5_6():
    for i in range(1, 101):
        print(i, len_3plus1(i))


if __name__ == '__main__':
    Q5_1()
    Q5_2()
    Q5_4()
    Q5_5()
    Q5_6()
