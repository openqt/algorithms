# coding=utf-8
"""
198. House Robber

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping
you from robbing each of them is that adjacent houses have security system
connected and it will automatically contact the police if two adjacent houses
were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without
alerting the police.
"""
from __future__ import print_function


class Solution(object):
    def rob(self, nums, cache=None):
        """
        :type nums: List[int]
        :rtype: int
        """
        if cache is None:
            cache = {}

        if len(nums) in cache:
            return cache[len(nums)]

        if len(nums) <= 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:  # 取前两个最大的再递推剩余数组
            total = max(nums[0] + self.rob(nums[2:], cache),
                        nums[1] + self.rob(nums[3:], cache))
            cache[len(nums)] = total  # cache最后一个值其实就是整个数组的最大值
            return total


if __name__ == '__main__':
    so = Solution()
    print(so.rob([2, 1, 1, 2]))  # 4
    print(so.rob([155, 44, 52, 58, 250, 225, 109, 118, 211, 73, 137, 96, 137,
                  89, 174, 66, 134, 26, 25, 205, 239, 85, 146, 73, 55, 6, 122,
                  196, 128, 50, 61, 230, 94, 208, 46, 243, 105, 81, 157, 89,
                  205, 78, 249, 203, 238, 239, 217, 212, 241, 242, 157, 79,
                  133, 66, 36, 165]))  # 4517
