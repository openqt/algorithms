# coding=utf-8
import unittest

"""1. Two Sum
https://leetcode.com/problems/two-sum/description/

Given an array of integers, return **indices** of the two numbers such that
they add up to a specific target.

You may assume that each input would have **_exactly_** one solution, and you
may not use the _same_ element twice.

**Example:**

    
    
    Given nums = [2, 7, 11, 15], target = 9,
    
    Because nums[ **0** ] + nums[ **1** ] = 2 + 7 = 9,
    return [ **0** , **1** ].


Similar Questions:
  3Sum (3sum)
  4Sum (4sum)
  Two Sum II - Input array is sorted (two-sum-ii-input-array-is-sorted)
  Two Sum III - Data structure design (two-sum-iii-data-structure-design)
  Subarray Sum Equals K (subarray-sum-equals-k)
  Two Sum IV - Input is a BST (two-sum-iv-input-is-a-bst)
"""


class Solution(unittest.TestCase):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def test(self):
        self.assertEqual(self.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(self.twoSum([3, 2, 7, 11, 15], 9), [1, 2])

        self.assertEqual(self.twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(self.twoSum([0, 4, 3, 0], 0), [0, 3])
        self.assertEqual(self.twoSum([-1, -2, -3, -4, -5], -8), [2, 4])

        self.assertEqual(self.twoSum(
            [230, 863, 916, 585, 981, 404, 316, 785, 88, 12, 70, 435, 384, 778, 887, 755, 740, 337,
             86, 92, 325, 422, 815, 650, 920, 125, 277, 336, 221, 847, 168, 23, 677, 61, 400, 136,
             874, 363, 394, 199, 863, 997, 794, 587, 124, 321, 212, 957, 764, 173, 314, 422, 927,
             783, 930, 282, 306, 506, 44, 926, 691, 568, 68, 730, 933, 737, 531, 180, 414, 751, 28,
             546, 60, 371, 493, 370, 527, 387, 43, 541, 13, 457, 328, 227, 652, 365, 430, 803, 59,
             858, 538, 427, 583, 368, 375, 173, 809, 896, 370, 789], 542), [28, 45])


if __name__ == "__main__":
    unittest.main()
