# coding=utf-8
"""
Reciprocal cycles
Problem 26

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
"""
from __future__ import print_function


def repetend(dividend, divisor):
    """repetend sequence

    :param dividend: dividend
    :param divisor: divisor
    :return: repetend sequence
    """
    multiple = 0
    while dividend * 10 ** multiple < divisor:
        multiple += 1

    body = []
    while dividend > 0:  # 被除数是0，表示已经被整除了
        quotient, dividend = divmod(dividend * 10 ** multiple, divisor)
        if quotient in body:  # 除法余数相同，除数相同，循环节出现
            break
        body.append(quotient)

    return ''.join(str(i).zfill(multiple) for i in body)


if __name__ == '__main__':
    print(max((len(repetend(1, i)), i) for i in range(2, 1000)))  # (2946, 983)

# Easy Prey: Solve twenty-five of the fifty easiest problems
