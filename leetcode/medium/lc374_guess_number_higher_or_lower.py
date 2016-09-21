# coding=utf-8
"""
374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong,
I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible
results (-1, 1, or 0):

    -1 : My number is lower
     1 : My number is higher
     0 : Congrats! You got it!

Example:
    n = 10, I pick 6.

    Return 6.
"""
from __future__ import print_function

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

_NUMBER = 9


def guess(num):
    if num == _NUMBER:
        return 0
    return -1 if _NUMBER < num else 1


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 0, n
        while low < high:  # 二分查找
            i = (low + high + 1) / 2
            ret = guess(i)
            if ret == 0:
                return i
            elif ret < 0:
                high = i
            else:
                low = i
        return low


if __name__ == '__main__':
    so = Solution()
    print(so.guessNumber(9))  # 3
