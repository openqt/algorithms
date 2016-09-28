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

    for i in range(3, int(n ** .5 + 1), 2):
        if n % i == 0:
            return False
    return True


def prime(stop=None):
    """generating prime

    :param stop: iteration
    :return: prime
    """
    yield 2
    if stop == 1:
        return

    val = 1
    count = 1
    while True:
        val += 2
        if is_prime(val):
            yield val

            count += 1
            if stop and count >= stop:
                break


if __name__ == '__main__':
    for i in prime(10001):
        pass
    print(i)  # 104743
