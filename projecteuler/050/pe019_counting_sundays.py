#!/usr/bin/env python
# coding=utf-8
"""
Counting Sundays
Problem 19

You are given the following information, but you may prefer to do some research
for yourself.

    1 Jan 1900 was a Monday.

    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.

    A leap year occurs on any year evenly divisible by 4, but not on a century
    unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""
from __future__ import print_function


def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


if __name__ == '__main__':
    n = 0
    total = 1  # 每个月第一天
    for i in range(1900, 2001):
        feb = 29 if is_leap_year(i) else 28
        for j in [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]:
            total += j
            if total % 7 == 0 and i > 1900:  # 1900年不计
                n += 1
    print(n)
