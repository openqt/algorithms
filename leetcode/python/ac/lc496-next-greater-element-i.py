# coding=utf-8
import unittest

"""496. Next Greater Element I
https://leetcode.com/problems/next-greater-element-i/description/

You are given two arrays **(without duplicates)** `nums1` and `nums2` where
`nums1`’s elements are subset of `nums2`. Find all the next greater numbers
for `nums1`'s elements in the corresponding places of `nums2`.

The Next Greater Number of a number **x** in `nums1` is the first greater
number to its right in `nums2`. If it does not exist, output -1 for this
number.

**Example 1:**  

    
    
    **Input:** **nums1** = [4,1,2], **nums2** = [1,3,4,2].
    **Output:** [-1,3,-1]
    **Explanation:**
        For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
        For number 1 in the first array, the next greater number for it in the second array is 3.
        For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
    

**Example 2:**  

    
    
    **Input:** **nums1** = [2,4], **nums2** = [1,2,3,4].
    **Output:** [3,-1]
    **Explanation:**
        For number 2 in the first array, the next greater number for it in the second array is 3.
        For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
    

**Note:**  

  1. All elements in `nums1` and `nums2` are unique.
  2. The length of both `nums1` and `nums2` would not exceed 1000.


Similar Questions:
  Next Greater Element II (next-greater-element-ii)
  Next Greater Element III (next-greater-element-iii)
  Daily Temperatures (daily-temperatures)
"""


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        vals = {i: -1 for i in nums2}
        stack = []
        for i in nums2:
            while stack and i > stack[-1]:
                vals[stack.pop()] = i
            stack.append(i)

        return [vals[i] for i in nums1]


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1])
        self.assertEqual(s.nextGreaterElement([2, 4], [1, 2, 3, 4]), [3, -1])


if __name__ == "__main__":
    unittest.main()
