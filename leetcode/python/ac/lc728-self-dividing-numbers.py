# coding=utf-8
import unittest

"""728. Self Dividing Numbers
https://leetcode.com/problems/self-dividing-numbers/description/

A _self-dividing number_ is a number that is divisible by every digit it
contains.

For example, 128 is a self-dividing number because `128 % 1 == 0`, `128 % 2 ==
0`, and `128 % 8 == 0`.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self
dividing number, including the bounds if possible.

**Example 1:**  

    
    
    **Input:** 
    left = 1, right = 22
    **Output:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    

**Note:**

* The boundaries of each input argument are `1 <= left <= right <= 10000`.


Similar Questions:
  Perfect Number (perfect-number)
"""


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [i for i in range(left, right+1) if self._dividing(i)]

    def _dividing(self, n):
        d = set()
        i = n
        while i > 0:
            d.add(i % 10)
            i //= 10
        if 0 in d: return False
        return all(n % i == 0 for i in d)


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.selfDividingNumbers(1, 22), [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])


if __name__ == "__main__":
    unittest.main()
