# coding=utf-8
import unittest

"""169. Majority Element
https://leetcode.com/problems/majority-element/description/

Given an array of size _n_ , find the majority element. The majority element
is the element that appears **more than** `⌊ n/2 ⌋` times.

You may assume that the array is non-empty and the majority element always
exist in the array.

**Example 1:**

    
    
    **Input:** [3,2,3]
    **Output:** 3

**Example 2:**

    
    
    **Input:** [2,2,1,1,1,2,2]
    **Output:** 2


Similar Questions:
  Majority Element II (majority-element-ii)
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)//2]



class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.majorityElement([3, 2, 3]), 3)
        self.assertEqual(s.majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)


if __name__ == "__main__":
    unittest.main()
