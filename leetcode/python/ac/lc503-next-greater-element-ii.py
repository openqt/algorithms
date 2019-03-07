# coding=utf-8
import unittest

"""503. Next Greater Element II
https://leetcode.com/problems/next-greater-element-ii/description/

Given a circular array (the next element of the last element is the first
element of the array), print the Next Greater Number for every element. The
Next Greater Number of a number x is the first greater number to its
traversing-order next in the array, which means you could search circularly to
find its next greater number. If it doesn't exist, output -1 for this number.

**Example 1:**  

    
    
    **Input:** [1,2,1]
    **Output:** [2,-1,2]
    **Explanation:** The first 1's next greater number is 2;  The number 2 can't find next greater number; The second 1's next greater number needs to search circularly, which is also 2.
    

**Note:** The length of given array won't exceed 10000.


Similar Questions:
  Next Greater Element I (next-greater-element-i)
  Next Greater Element III (next-greater-element-iii)
"""


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = nums*2
        vals = [-1]*len(nums)
        stack = []
        for n, i in enumerate(nums):
            while stack and i > stack[-1][0]:
                t = stack.pop()
                vals[t[1]] = i
            stack.append((i, n))
        return vals[:len(vals)//2]


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.nextGreaterElements([1, 2, 1]), [2, -1, 2])


if __name__ == "__main__":
    unittest.main()
