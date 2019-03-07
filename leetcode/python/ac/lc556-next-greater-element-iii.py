# coding=utf-8
import unittest

"""556. Next Greater Element III
https://leetcode.com/problems/next-greater-element-iii/description/

Given a positive **32-bit** integer **n** , you need to find the smallest
**32-bit** integer which has exactly the same digits existing in the integer
**n** and is greater in value than n. If no such positive **32-bit** integer
exists, you need to return -1.

**Example 1:**

    
    
    **Input:** 12
    **Output:** 21
    



**Example 2:**

    
    
    **Input:** 21
    **Output:** -1


Similar Questions:
  Next Greater Element I (next-greater-element-i)
  Next Greater Element II (next-greater-element-ii)
"""


class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = list(str(n))

        # 从排列的右端开始，找出第一个比右边数字小的数字的序号j
        i = len(s)-1
        while i > 0 and s[i-1] >= s[i]:
            i -= 1
        if i <= 0: return -1
        j = i - 1

        # 在Pj的右边的数字中，找出所有比Pj大的数字中最小的数字Pk
        k = len(s)-1
        while s[k] <= s[j]:
            k -= 1

        # 交换Pj，Pk
        s[k], s[j] = s[j], s[k]

        # 再将排列右端的递减部分Pj+1Pj+2……Pn倒转，因为j右端的数字是降序，所以只需要其左边和右边的交换，直到中间
        r = len(s)-1
        while i < r:
            s[i], s[r] = s[r], s[i]
            i += 1
            r -= 1

        n2 = int(''.join(s))
        if n2 > 0x7fffffff: return -1
        return n2

        
class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.nextGreaterElement(12), 21)
        self.assertEqual(s.nextGreaterElement(21), -1)
        self.assertEqual(s.nextGreaterElement(346987521), 347125689)
        self.assertEqual(s.nextGreaterElement(231), 312)
        self.assertEqual(s.nextGreaterElement(1999999999), -1)
        self.assertEqual(s.nextGreaterElement(2147483647), -1)


if __name__ == "__main__":
    unittest.main()
