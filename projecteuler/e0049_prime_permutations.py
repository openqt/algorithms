# coding=utf-8
"""
Prime permutations
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways:
    (i) each of the three terms are prime, and,
    (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""
from __future__ import print_function
from e0003_largest_prime_factor import prime_sieve


if __name__ == '__main__':
    caches = {}
    for i in prime_sieve(10000):
        if i > 1000 and len(set(str(i))) == 4:  # 四位质数并且各位数字不重复
            key = ''.join(sorted(str(i)))
            caches.setdefault(key, []).append(i)  # 按排序分组，默认即升序

    for v in caches.values():
        if len(v) >= 3:  # 需要满足最少有3个质数
            diff = [v[i] - v[i-1] for i in range(1, len(v))]  # 先计算数字之差
            for i in range(1, len(diff)):
                if diff[i] == diff[i-1]:  # 如果有连续的差值相等，则是要找的序列
                    print(v)
                    break
