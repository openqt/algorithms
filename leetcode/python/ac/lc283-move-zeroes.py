# coding=utf-8
import unittest

"""283. Move Zeroes
https://leetcode.com/problems/move-zeroes/description/

Given an array `nums`, write a function to move all `0`'s to the end of it
while maintaining the relative order of the non-zero elements.

**Example:**

    
    
    **Input:** [0,1,0,3,12]
    **Output:** [1,3,12,0,0]

**Note** :

  1. You must do this **in-place** without making a copy of the array.
  2. Minimize the total number of operations.


Similar Questions:
  Remove Element (remove-element)
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
        for i in range(pos, len(nums)):
            nums[i] = 0


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        data = [0, 1, 0, 3, 12]
        s.moveZeroes(data)
        self.assertEqual(data, [1, 3, 12, 0, 0])


if __name__ == "__main__":
    unittest.main()
