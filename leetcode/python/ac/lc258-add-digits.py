# coding=utf-8
import unittest

"""258. Add Digits
https://leetcode.com/problems/add-digits/description/

Given a non-negative integer `num`, repeatedly add all its digits until the
result has only one digit.

**Example:**

    
    
    **Input:** 38
    **Output:** 2 
    **Explanation:** The process is like: 3 + 8 = 11, 1 + 1 = 2. 
                 Since 2 has only one digit, return it.
    

**Follow up:**  
Could you do it without any loop/recursion in O(1) runtime?


Similar Questions:
  Happy Number (happy-number)
"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            num = self._calc(num)
        return num
        
    def _calc(self, n):
        val = 0
        while n > 0:
            val += n % 10
            n //= 10
        return val


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.addDigits(38), 2)


if __name__ == "__main__":
    unittest.main()
