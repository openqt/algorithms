# coding=utf-8
import unittest

"""456. 132 Pattern
https://leetcode.com/problems/132-pattern/description/

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence
a **i** , a **j** , a **k** such that **i** < **j** < **k** and a **i** < a
**k** < a **j**. Design an algorithm that takes a list of n numbers as input
and checks whether there is a 132 pattern in the list.

**Note:** n will be less than 15,000.

**Example 1:**  

    
    
    **Input:** [1, 2, 3, 4]
    
    **Output:** False
    
    **Explanation:** There is no 132 pattern in the sequence.
    

**Example 2:**  

    
    
    **Input:** [3, 1, 4, 2]
    
    **Output:** True
    
    **Explanation:** There is a 132 pattern in the sequence: [1, 4, 2].
    

**Example 3:**  

    
    
    **Input:** [-1, 3, 2, 0]
    
    **Output:** True
    
    **Explanation:** There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].


Similar Questions:

"""


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        return False


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(s.find132pattern([3, 5, 0, 3, 4]))
        self.assertFalse(s.find132pattern([1, 0, 1, -4, -3]))
        self.assertFalse(s.find132pattern([1, 2, 3, 4]))
        self.assertTrue(s.find132pattern([3, 1, 4, 2]))
        self.assertTrue(s.find132pattern([-1, 3, 2, 0]))


if __name__ == "__main__":
    unittest.main()
