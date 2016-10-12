"""
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from __future__ import print_function


def is_prime(n):
    """check a number is a prime

    :return: True for prime
    """
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False

    for i in xrange(3, int(n ** .5 + 1), 2):
        if n % i == 0:
            return False
    return True


def prime(start=1, stop=-1):
    """generating prime

    :param start: start
    :param stop: the maximum primes
    :return: prime
    """
    yield 2

    if start % 2 == 0:
        start -= 1  # ensure odd

    while True:
        start += 2
        if is_prime(start):
            yield start

            stop -= 1
            if stop == 1:
                break


if __name__ == '__main__':
    for i in prime(stop=10001):
        pass
    print(i)  # 104743
