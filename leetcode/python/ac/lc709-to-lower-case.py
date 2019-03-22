# coding=utf-8
import unittest

"""709. To Lower Case
https://leetcode.com/problems/to-lower-case/description/

Implement function ToLowerCase() that has a string parameter str, and returns
the same string in lowercase.



**Example 1:**

    
    
    **Input:** "Hello"
    **Output:** "hello"
    

**Example 2:**

    
    
    **Input:** "here"
    **Output:** "here"
    

**Example 3:**

    
    
    **Input:** "LOVELY"
    **Output:** "lovely"


Similar Questions:

"""


class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()

    class T(unittest.TestCase):
        def test(self):
            s = Solution()
            self.assertEqual(s.toLowerCase("Hello"), "hello")
            self.assertEqual(s.toLowerCase("here"), "here")
            self.assertEqual(s.toLowerCase("LOVELY"), "lovely")


if __name__ == "__main__":
    unittest.main()
