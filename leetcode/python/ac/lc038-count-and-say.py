# coding=utf-8
import unittest

"""38. Count and Say
https://leetcode.com/problems/count-and-say/description/

The count-and-say sequence is the sequence of integers with the first five
terms as following:

    
    
    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    

`1` is read off as `"one 1"` or `11`.  
`11` is read off as `"two 1s"` or `21`.  
`21` is read off as `"one 2`, then `one 1"` or `1211`.  

Given an integer _n_ , generate the _n_ th term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

**Example 1:**

    
    
    **Input:** 1
    **Output:** "1"
    

**Example 2:**

    
    
    **Input:** 4
    **Output:** "1211"


Similar Questions:
  Encode and Decode Strings (encode-and-decode-strings)
  String Compression (string-compression)
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        val = "1"
        for i in range(1, n):
            val = self._say(val)
        return val

    def _say(self, s):
        val = ""
        total, c = 1, s[0]
        for i in range(1, len(s)):
            if s[i] == c:
                total += 1
            else:
                val += "%d%s" % (total, c)
                c = s[i]
                total = 1
        val += "%d%s" % (total, c)
        return val


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.countAndSay(1), "1")
        self.assertEqual(s.countAndSay(2), "11")
        self.assertEqual(s.countAndSay(3), "21")
        self.assertEqual(s.countAndSay(4), "1211")
        self.assertEqual(s.countAndSay(5), "111221")
        self.assertEqual(s.countAndSay(6), "312211")


if __name__ == "__main__":
    unittest.main()
