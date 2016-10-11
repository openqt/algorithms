# coding=utf-8
"""
Pandigital multiples
Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
from __future__ import print_function


def is_pandigital(n):
    """if a number is a pandigital

    :param n: number
    :return: True or False
    """
    if 1e8 < n < 1e9:
        map = [False] * 10
        map[0] = True  # 0 is occurred by default
        while n > 0:
            n, div = divmod(n, 10)
            if map[div]:
                return False
            else:
                map[div] = True
        return True
    return False


if __name__ == '__main__':
    val = ''
    for i in range(1, 10000):
        s = ''
        for j in range(1, 10):
            s += str(i * j)
            if len(s) >= 9 and is_pandigital(int(s)):
                print('{} (1..{}) = {}'.format(i, j, s))
                val = max(val, s)
    print(val)  # 932718654
