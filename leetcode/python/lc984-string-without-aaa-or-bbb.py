# coding=utf-8
import unittest

"""984. String Without AAA or BBB
https://leetcode.com/problems/string-without-aaa-or-bbb/description/

Given two integers `A` and `B`, return **any** string `S` such that:

  * `S` has length `A + B` and contains exactly `A` `'a'` letters, and exactly `B` `'b'` letters;
  * The substring `'aaa'` does not occur in `S`;
  * The substring `'bbb'` does not occur in `S`.



**Example 1:**

    
    
    **Input:** A = 1, B = 2
    **Output:** "abb"
    **Explanation:**  "abb", "bab" and "bba" are all correct answers.
    

**Example 2:**

    
    
    **Input:** A = 4, B = 1
    **Output:** "aabaa"



**Note:**

  1. `0 <= A <= 100`
  2. `0 <= B <= 100`
  3. It is guaranteed such an `S` exists for the given `A` and `B`.


Similar Questions:

"""


class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
