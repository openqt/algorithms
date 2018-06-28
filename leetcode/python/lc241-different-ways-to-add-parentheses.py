# coding=utf-8
import unittest

"""241. Different Ways to Add Parentheses
https://leetcode.com/problems/different-ways-to-add-parentheses/description/

Given a string of numbers and operators, return all possible results from
computing all the different possible ways to group numbers and operators. The
valid operators are `+`, `-` and `*`.

**Example 1:**

    
    
    **Input:** "2-1-1"
    **Output:** [0, 2]
    **Explanation:**
    ((2-1)-1) = 0 
    (2-(1-1)) = 2

**Example 2:**

    
    
    **Input:**"2*3-4*5"
    **Output:** [-34, -14, -10, -10, 10]
    **Explanation:** (2*(3-(4*5))) = -34 
    ((2*3)-(4*5)) = -14 
    ((2*(3-4))*5) = -10 
    (2*((3-4)*5)) = -10 
    (((2*3)-4)*5) = 10 ****


Similar Questions:
  Unique Binary Search Trees II (unique-binary-search-trees-ii)
  Basic Calculator (basic-calculator)
  Expression Add Operators (expression-add-operators)
"""


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
