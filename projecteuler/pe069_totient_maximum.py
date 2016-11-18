# coding=utf-8
"""
Totient maximum
Problem 69

Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
prime to nine, φ(9)=6.

    n	Relatively Prime	φ(n)	n/φ(n)
    2	1	                1   	2
    3	1,2	                2   	1.5
    4	1,3	                2	    2
    5	1,2,3,4	            4	    1.25
    6	1,5	                2   	3
    7	1,2,3,4,5,6	        6   	1.1666...
    8	1,3,5,7	            4   	2
    9	1,2,4,5,7,8	        6   	1.5
    10	1,3,7,9	            4   	2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""
from __future__ import print_function, division
# from pe003_largest_prime_factor import prime_sieve
from pe007_10001st_primes import prime


def totient(n, *args):
    """relatively prime to n

    欧拉函数有一个简单的计算公式: 找出所有能被n整除的质数p，然后计算出1−1/p的连乘，再乘以n
        ϕ(n)=n∏p|n (1−1/p)
    :param n: the number
    :return: phi
    """
    if n <= 1:
        return 1

    # vals = args if args else [i for i in prime_sieve(n) if n % i == 0]
    # return int(reduce(lambda x, y: x - x / y, vals, n)) if vals else n - 1

    m, p = n, 2
    while p * p <= n:
        k = 0

        while n % p == 0:
            k += 1
            n /= p

        if k > 0:
            m *= (p - 1) / p
            # m *= p ** (k - 1) * (p - 1)

        p += 1

    if n > 1:
        m *= (n - 1) / n
        # m *= n - 1

    return int(m)


if __name__ == '__main__':
    # print(max((i / totient(i), i) for i in range(2, 1000000, 2)))
    # exit(0)

    """
    http://www.kylen314.com/archives/4943

    这道题有一个很容易想到的纯手算方法，从上面计算ϕ(n)的公式我们就可以得到:
        n/ϕ(n)=∏p|n p/(p−1)

    注意这里p是质数，而p/(p−1)>1，所以一个数n，含有的可以整除的质数越多，那么这个数的的
    n/ϕ(n)就越大，所以可以得到2×3×5×7×11×13×17=510510<1,000,000 是最大的解！！
    """
    total = 1
    for i in prime():
        if total * i > 1000000:
            print(total, total / totient(total))  # 510510 5.53938802083
            break
        else:
            total *= i
