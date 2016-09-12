# coding=utf-8
"""
164. Maximum Gap

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
"""
from leetcode.utils.funcs import print_result


class Solution(object):

    @print_result
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # TODO: O(n) 研究O(n)的解法


    @print_result
    def maximumGap1(self, nums):
        """这个问题在实际工程中的解法，简单直接
        :type nums: List[int]
        :rtype: int
        """
        gap = 0
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if (nums[i] - nums[i-1]) > gap:
                gap = nums[i] - nums[i-1]
        return gap


if __name__ == '__main__':
    s = Solution()
    assert s.maximumGap([1]) == 0
    assert s.maximumGap([3, 7, 6, 2]) == 3
