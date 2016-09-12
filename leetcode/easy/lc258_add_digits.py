#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Add Digits
https://leetcode.com/problems/add-digits/

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Hint::

    A naive implementation of the above process is trivial. Could you come up with other methods?
    What are all the possible results?
    How do they occur, periodically or randomly?
    You may find this Wikipedia article useful.
"""
import unittest

__version__ = "2015.1217.1"  # year.day.revision


class Solution(unittest.TestCase):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        pass

    def test(self):
        assert self.addDigits(38) == 2


if __name__ == '__main__':
    unittest.main()
