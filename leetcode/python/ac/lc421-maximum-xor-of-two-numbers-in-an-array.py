# coding=utf-8
import unittest

"""421. Maximum XOR of Two Numbers in an Array
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/

Given a **non-empty** array of numbers, a 0, a1, a2, … , an-1, where 0 ≤ ai <
231.

Find the maximum result of ai XOR aj, where 0 ≤ _i_ , _j_ < _n_.

Could you do this in O( _n_ ) runtime?

**Example:**

    
    
    **Input:** [3, 10, 5, 25, 2, 8]
    
    **Output:** 28
    
    **Explanation:** The maximum result is **5** ^ **25** = 28.


Similar Questions:

"""


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val, mask = 0, 0
        for i in reversed(range(32)):
            mask |= 1 << i  # 高位全是1
            val |= 1 << i  # 高位是最终结果的排列
            cache = set([(n & mask) for n in nums])
            for key in cache:
                if val ^ key in cache:
                    break
            else:
                val &= val - 1  # 去掉最后的1

        print(nums, bin(val), val)
        return val


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.findMaximumXOR([14, 11, 7, 2]), 12)
        self.assertEqual(s.findMaximumXOR([3, 10, 5, 25, 2, 8]), 28)


if __name__ == "__main__":
    unittest.main()
