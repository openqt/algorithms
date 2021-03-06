# coding=utf-8
import unittest

"""321. Create Maximum Number
https://leetcode.com/problems/create-maximum-number/description/

Given two arrays of length `m` and `n` with digits `0-9` representing two
numbers. Create the maximum number of length `k <= m + n` from digits of the
two. The relative order of the digits from the same array must be preserved.
Return an array of the `k` digits.

**Note:** You should try to optimize your time and space complexity.

**Example 1:**

    
    
    **Input:**
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5
    **Output:**
    [9, 8, 6, 5, 3]

**Example 2:**

    
    
    **Input:**
    nums1 = [6, 7]
    nums2 = [6, 0, 4]
    k = 5
    **Output:**
    [6, 7, 6, 0, 4]

**Example 3:**

    
    
    **Input:**
    nums1 = [3, 9]
    nums2 = [8, 9]
    k = 3
    **Output:**
    [9, 8, 9]


Similar Questions:
  Remove K Digits (remove-k-digits)
  Maximum Swap (maximum-swap)
"""


class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
