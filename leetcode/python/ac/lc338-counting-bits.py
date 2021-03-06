# coding=utf-8
import unittest

"""338. Counting Bits
https://leetcode.com/problems/counting-bits/description/

Given a non negative integer number **num**. For every numbers **i** in the
range **0 ≤ i ≤ num** calculate the number of 1's in their binary
representation and return them as an array.

**Example:** For `num = 5` you should return `[0,1,1,2,1,2]`.

**Follow up:**

  * It is very easy to come up with a solution with run time **O(n*sizeof(integer))**. But can you do it in linear time **O(n)** /possibly in a single pass?
  * Space complexity should be **O(n)**.
  * Can you do it like a boss? Do it without using any builtin function like **__builtin_popcount** in c++ or in any other language.

**Credits:**  
Special thanks to [@ syedee ](https://leetcode.com/discuss/user/syedee) for
adding this problem and creating all test cases.


Similar Questions:
  Number of 1 Bits (number-of-1-bits)
"""


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        val = [0] * (num + 1)
        for i in range(1, len(val)):
            val[i] = val[i & (i - 1)] + 1
        return val


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.countBits(5), [0, 1, 1, 2, 1, 2])


if __name__ == "__main__":
    unittest.main()
