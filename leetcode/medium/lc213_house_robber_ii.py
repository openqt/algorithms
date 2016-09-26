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
        max_val = 0
        for loop in range(len(nums)):  # 按环内每个元素作为起始位置开始计算
            amounts = [0, nums[loop]]  # 每个元素都算作开始
            for i in range(1, len(nums) - 1):  # 环内最后一个元素去掉，因为与头相邻
                amounts.append(
                    max(nums[(i + loop) % len(nums)] + amounts[i - 1],
                        amounts[i]))
            max_val = max(max_val, amounts[-1])  # 取每次计算的最大值

        return max_val


if __name__ == '__main__':
    so = Solution()
    print(so.rob([1]))  # 1
    print(so.rob([1, 1, 1]))  # 1
    print(so.rob([2, 1, 1, 2]))  # 3
    print(so.rob([155, 44, 52, 58, 250, 225, 109, 118, 211, 73, 137, 96, 137,
                  89, 174, 66, 134, 26, 25, 205, 239, 85, 146, 73, 55, 6, 122,
                  196, 128, 50, 61, 230, 94, 208, 46, 243, 105, 81, 157, 89,
                  205, 78, 249, 203, 238, 239, 217, 212, 241, 242, 157, 79,
                  133, 66, 36, 165]))  # 4388
