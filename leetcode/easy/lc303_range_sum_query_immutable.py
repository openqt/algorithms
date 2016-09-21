# coding=utf-8
"""
303. Range Sum Query - Immutable

Given an integer array nums, find the sum of the elements between indices i
and j (i ≤ j), inclusive.

Example:
    Given nums = [-2, 0, 3, -5, 2, -1]

    sumRange(0, 2) -> 1
    sumRange(2, 5) -> -1
    sumRange(0, 5) -> -3

Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""
from __future__ import print_function


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.integral = [0, ]  # 一维积分图
        if nums:
            n = 0
            for i in nums:
                n += i
                self.integral.append(n)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.integral[j+1] - self.integral[i]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

if __name__ == '__main__':
    so = NumArray([-2, 0, 3, -5, 2, -1])
    print(so.integral)
    print(so.sumRange(0, 2))  # 1
    print(so.sumRange(2, 5))  # -1
    print(so.sumRange(0, 5))  # -3
