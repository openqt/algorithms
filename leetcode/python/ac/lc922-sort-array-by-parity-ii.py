# coding=utf-8
import unittest

"""922. Sort Array By Parity II
https://leetcode.com/problems/sort-array-by-parity-ii/description/

Given an array `A` of non-negative integers, half of the integers in A are
odd, and half of the integers are even.

Sort the array so that whenever `A[i]` is odd, `i` is odd; and whenever `A[i]`
is even, `i` is even.

You may return any answer array that satisfies this condition.



**Example 1:**

    
    
    **Input:** [4,2,5,7]
    **Output:** [4,5,2,7]
    **Explanation:** [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
    



**Note:**

  1. `2 <= A.length <= 20000`
  2. `A.length % 2 == 0`
  3. `0 <= A[i] <= 1000`


Similar Questions:

"""


class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, 1
        while True:
            while i < len(A) and A[i] % 2 == 0:
                i += 2
            while j < len(A) and A[j] % 2 == 1:
                j += 2

            if i < len(A) and j < len(A):
                A[i], A[j] = A[j], A[i]
            else:
                break
        return A


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.sortArrayByParityII([4, 2, 5, 7]), [4, 5, 2, 7])
        self.assertEqual(s.sortArrayByParityII([888, 505, 627, 846]), [888, 505, 846, 627])


if __name__ == "__main__":
    unittest.main()
