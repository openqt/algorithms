# coding=utf-8
"""
368. Largest Divisible Subset

Given a set of distinct positive integers, find the largest subset such that
every pair (Si, Sj) of elements in this subset satisfies:
    Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

    nums: [1,2,3]

    Result: [1,2] (of course, [1,3] will also be ok)

Example 2:

    nums: [1,2,4,8]

    Result: [1,2,4,8]
"""
from __future__ import print_function


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """




if __name__ == '__main__':
    so = Solution()
    print(so.largestDivisibleSubset([1, 2, 3]))  # [1, 2]
    print(so.largestDivisibleSubset([1, 2, 4, 8]))  # [1, 2, 4, 8]
