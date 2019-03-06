# coding=utf-8
import unittest

"""191. Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/description/

Write a function that takes an unsigned integer and returns the number of '1'
bits it has (also known as the [Hamming
weight](http://en.wikipedia.org/wiki/Hamming_weight)).

**Example 1:**

    
    
    **Input:** 11
    **Output:** 3
    **Explanation:** Integer 11 has binary representation **00000000000000000000000000001011**
    

**Example 2:**

    
    
    **Input:** 128
    **Output:** 1
    **Explanation:** Integer 128 has binary representation **00000000000000000000000010000000**


Similar Questions:
  Reverse Bits (reverse-bits)
  Power of Two (power-of-two)
  Counting Bits (counting-bits)
  Binary Watch (binary-watch)
  Hamming Distance (hamming-distance)
  Binary Number with Alternating Bits (binary-number-with-alternating-bits)
  Prime Number of Set Bits in Binary Representation (prime-number-of-set-bits-in-binary-representation)
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        val = 0
        while n > 0:
            val += 1
            n &= n - 1
        return val
        

class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.hammingWeight(0b00000000000000000000000000001011), 3)
        self.assertEqual(s.hammingWeight(0b00000000000000000000000010000000), 1)
        self.assertEqual(s.hammingWeight(0b11111111111111111111111111111101), 31)


if __name__ == "__main__":
    unittest.main()
