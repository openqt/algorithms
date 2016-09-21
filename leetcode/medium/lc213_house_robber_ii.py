# coding=utf-8
"""
213. House Robber II

Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new
place for his thievery so that he will not get too much attention.
This time, all houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, the security system for these houses remain the same as for those
in the previous street.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without
alerting the police.
"""
from __future__ import print_function


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(nums)
        amounts = [0, nums[0]]
        for i in range(1, len(nums)):
            amounts.append(max(nums[i]+amounts[i-1], amounts[i]))
        return amounts[-1]


if __name__ == '__main__':
    so = Solution()
    print(so.rob([2, 1, 1, 2]))  # 4
    print(so.rob([155, 44, 52, 58, 250, 225, 109, 118, 211, 73, 137, 96, 137,
                  89, 174, 66, 134, 26, 25, 205, 239, 85, 146, 73, 55, 6, 122,
                  196, 128, 50, 61, 230, 94, 208, 46, 243, 105, 81, 157, 89,
                  205, 78, 249, 203, 238, 239, 217, 212, 241, 242, 157, 79,
                  133, 66, 36, 165]))  # 4517
