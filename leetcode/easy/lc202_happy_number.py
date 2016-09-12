#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Happy Number
https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""
import unittest

__version__ = "2015.1214.1"  # year.day.revision


class Solution(unittest.TestCase):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        steps = set()
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n in steps: return False
            steps.add(n)
        return True

    def test(self):
        assert self.isHappy(19)
        assert not self.isHappy(20)


if __name__ == '__main__':
    unittest.main()
