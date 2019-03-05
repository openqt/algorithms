# coding=utf-8
import unittest

"""374. Guess Number Higher or Lower
https://leetcode.com/problems/guess-number-higher-or-lower/description/

We are playing the Guess Game. The game is as follows:

I pick a number from **1** to **_n_**. You have to guess which number I
picked.

Every time you guess wrong, I'll tell you whether the number is higher or
lower.

You call a pre-defined API `guess(int num)` which returns 3 possible results
(`-1`, `1`, or `0`):

    
    
    -1 : My number is lower
     1 : My number is higher
     0 : Congrats! You got it!
    

**Example:**  

    
    
    n = 10, I pick 6.
    
    Return 6.


Similar Questions:
  First Bad Version (first-bad-version)
  Guess Number Higher or Lower II (guess-number-higher-or-lower-ii)
  Find K Closest Elements (find-k-closest-elements)
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    pick = 6
    if pick < num: return -1
    if pick > num: return 1
    return 0


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            m = int((r + l) / 2)
            if guess(m) < 0:
                r = m
            elif guess(m) > 0:
                l = m + 1
            else:
                return m
        return l


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.guessNumber(10), 6)


if __name__ == "__main__":
    unittest.main()
