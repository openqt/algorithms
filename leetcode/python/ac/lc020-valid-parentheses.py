# coding=utf-8
import unittest

"""20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/

Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`,
`'['` and `']'`, determine if the input string is valid.

An input string is valid if:

  1. Open brackets must be closed by the same type of brackets.
  2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

**Example 1:**

    
    
    **Input:**  "()"
    **Output:** true
    

**Example 2:**

    
    
    **Input:**  "()[]{}"
    **Output:** true
    

**Example 3:**

    
    
    **Input:**  "(]"
    **Output:** false
    

**Example 4:**

    
    
    **Input:**  "([)]"
    **Output:** false
    

**Example 5:**

    
    
    **Input:**  "{[]}"
    **Output:** true


Similar Questions:
  Generate Parentheses (generate-parentheses)
  Longest Valid Parentheses (longest-valid-parentheses)
  Remove Invalid Parentheses (remove-invalid-parentheses)
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        MAP = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i in s:
            if i in MAP:
                stack.append(i)
            else:
                if not stack or MAP[stack.pop()] != i:
                    return False
        return len(stack) == 0


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(s.isValid("()"))
        self.assertTrue(s.isValid("()[]{}"))
        self.assertFalse(s.isValid("(]"))
        self.assertFalse(s.isValid("([)]"))
        self.assertTrue(s.isValid("{[]}"))


if __name__ == "__main__":
    unittest.main()
