# coding=utf-8
import unittest

"""906. Super Palindromes
https://leetcode.com/problems/super-palindromes/description/

Let's say a positive integer is a  _superpalindrome_  if it is a palindrome,
and it is also the square of a palindrome.

Now, given two positive integers `L` and `R` (represented as strings), return
the number of superpalindromes in the inclusive range `[L, R]`.



**Example 1:**

    
    
    **Input:** L = "4", R = "1000"
    **Output:** 4
    **Explanation** : 4, 9, 121, and 484 are superpalindromes.
    Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.



**Note:**

  1. `1 <= len(L) <= 18`
  2. `1 <= len(R) <= 18`
  3. `L` and `R` are strings representing integers in the range `[1, 10^18)`.
  4. `int(L) <= int(R)`


Similar Questions:

"""


class Solution(object):
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
