#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Nim Game
https://leetcode.com/problems/nim-game/

You are playing the following Nim Game with your friend:
There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones.
The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game.
Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game:

Hint::

    If there are 5 stones in the heap,
    could you figure out a way to remove the stones such that you will always be the winner?
"""
import unittest

__version__ = "2015.1217.1"  # year.day.revision


class Solution(unittest.TestCase):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0

    def test(self):
        assert not self.canWinNim(4)
        assert self.canWinNim(5)
        assert self.canWinNim(6)
        assert not self.canWinNim(8)
        assert not self.canWinNim(1348820612)


if __name__ == '__main__':
    unittest.main()
