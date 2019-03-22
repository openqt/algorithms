# coding=utf-8
import unittest

"""678. Valid Parenthesis String
https://leetcode.com/problems/valid-parenthesis-string/description/

Given a string containing only three types of characters: '(', ')' and '*',
write a function to check whether this string is valid. We define the validity
of a string by these rules:

  1. Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
  2. Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
  3. Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
  4. `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or an empty string.
  5. An empty string is also valid.

**Example 1:**  

    
    
    **Input:** "()"
    **Output:** True
    

**Example 2:**  

    
    
    **Input:** "(*)"
    **Output:** True
    

**Example 3:**  

    
    
    **Input:** "(*))"
    **Output:** True
    

**Note:**  

  1. The string size will be in the range [1, 100].


Similar Questions:
  Special Binary String (special-binary-string)
"""


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self._check(0., s)

    def _check(self, stack, s):
        for n, i in enumerate(s):
            if i == '(':
                stack += 1
            elif i == ')':
                stack -= 1
                if stack < 0:
                    return False
            else:  # *
                return self._check(stack-1, s[n+1:]) or self._check(stack, s[n+1:]) or self._check(stack+1, s[n+1:])
        return stack == 0


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertFalse(s.checkValidString(")("))

        self.assertTrue(s.checkValidString("()"))
        self.assertTrue(s.checkValidString("(*)"))
        self.assertTrue(s.checkValidString("(*))"))

        # self.assertFalse(s.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))
        self.assertFalse(s.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))


if __name__ == "__main__":
    unittest.main()
