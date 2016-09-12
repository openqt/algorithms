#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Ugly Number II
https://leetcode.com/problems/ugly-number-ii/

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.

Hint::

    1. The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly.
    Try to focus your effort on generating only the ugly ones.

    2. An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.

    3. The key is how to maintain the order of the ugly numbers.
    Try a similar approach of merging from three sorted lists: L1, L2, and L3.

    4. Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).
"""
import unittest

__version__ = "2015.1215.1"  # year.day.revision


class SortedSet(object):
    def __init__(self, *seq):
        self.seq = list(seq)
        self.set = set(self.seq)

    def pop(self):
        k = self.seq.pop()
        self.set.remove(k)
        return k

    def push(self, k):
        if k not in self.set:
            self.seq.append(k)
            self.seq.sort(reverse=True)
            self.set.add(k)

    def __str__(self):
        return ', '.join(str(i) for i in self.seq)


class Solution(unittest.TestCase):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ss = SortedSet(1)
        kth = 1
        while n > 0:
            kth = ss.pop()
            ss.push(kth * 2)
            ss.push(kth * 3)
            ss.push(kth * 5)

            n -= 1
        return kth

    def test(self):
        assert self.nthUglyNumber(2) == 2
        assert self.nthUglyNumber(9) == 10
        assert self.nthUglyNumber(10) == 12
        assert self.nthUglyNumber(1297) == 301989888


if __name__ == '__main__':
    unittest.main()
