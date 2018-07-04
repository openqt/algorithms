# coding=utf-8
import unittest

"""4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/description/

There are two sorted arrays **nums1** and **nums2** of size m and n
respectively.

Find the median of the two sorted arrays. The overall run time complexity
should be O(log (m+n)).

**Example 1:**  

    
    
    nums1 = [1, 3]
    nums2 = [2]
    
    The median is 2.0
    

**Example 2:**  

    
    
    nums1 = [1, 2]
    nums2 = [3, 4]
    
    The median is (2 + 3)/2 = 2.5


Similar Questions:

"""


class Solution(unittest.TestCase):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (len(nums1) + len(nums2)) % 2 == 0:  # even
            pass
        else:  # odd
            pass

    def test(self):
        self.assertEqual(self.findMedianSortedArrays([1, 3], [2]), 2.0)
        self.assertEqual(self.findMedianSortedArrays([1, 2], [3, 4]), 2.5)


if __name__ == "__main__":
    unittest.main()
