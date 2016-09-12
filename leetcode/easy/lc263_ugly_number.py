#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Ugly Number
https://leetcode.com/problems/ugly-number/

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
"""
import unittest

__version__ = "2015.1214.1"  # year.day.revision


class Solution(unittest.TestCase):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        if num == 1: return True

        for i in (2, 3, 5):
            while num > 1 and num % i ==0:
                num /= i
        return num == 1

    def test(self):
        assert self.isUgly(1)
        assert self.isUgly(6)
        assert self.isUgly(8)
        assert not self.isUgly(14)


if __name__ == '__main__':
    unittest.main()
