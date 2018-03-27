from __future__ import division
import unittest


class Solution(unittest.TestCase):
    """4. Median of Two Sorted Arrays

    There are two sorted arrays nums1 and nums2 of size m and n respectively.

    Find the median of the two sorted arrays. The overall run time complexity
    should be O(log (m+n)).

    Example 1:
        nums1 = [1, 3]
        nums2 = [2]

        The median is 2.0

    Example 2:
        nums1 = [1, 2]
        nums2 = [3, 4]

        The median is (2 + 3)/2 = 2.5
    """

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def virtual_list(i):
            return nums1[i] if i < len(nums1) else nums2[i - len(nums1)]

        length = len(nums1) + len(nums2)

        if nums1[0] > nums2[0]:
            nums1, nums2 = nums2, nums1

        if nums1[-1] < nums2[0]:
            if length % 2 == 1:
                return virtual_list(int(length / 2))
            else:
                n = int(length / 2)
                return (virtual_list(n) + virtual_list(n - 1)) / 2
        else:
            pass

    def test(self):
        self.assertEqual(self.findMedianSortedArrays([1, 3], [2]), 2.0)
        self.assertEqual(self.findMedianSortedArrays([1, 2], [3, 4]), 2.5)


if __name__ == '__main__':
    unittest.main()
