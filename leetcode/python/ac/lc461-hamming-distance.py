# coding=utf-8
import unittest

"""461. Hamming Distance
https://leetcode.com/problems/hamming-distance/description/

The [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance) between
two integers is the number of positions at which the corresponding bits are
different.

Given two integers `x` and `y`, calculate the Hamming distance.

**Note:**  
0  ≤ `x`, `y` < 231.

**Example:**

    
    
    **Input:** x = 1, y = 4
    
    **Output:** 2
    
    **Explanation:**
    1   (0 0 0 1)
    4   (0 1 0 0)
            ↑   ↑
    
    The above arrows point to positions where the corresponding bits are different.


Similar Questions:
  Number of 1 Bits (number-of-1-bits)
  Total Hamming Distance (total-hamming-distance)
"""


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        d = 0
        while x > 0 or y > 0:
            d += (x & 1) ^ (y & 1)
            x >>= 1
            y >>= 1
        return d


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.hammingDistance(1, 4), 2)


if __name__ == "__main__":
    unittest.main()
