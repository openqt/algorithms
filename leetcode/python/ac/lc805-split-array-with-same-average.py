# coding=utf-8
import unittest

"""805. Split Array With Same Average
https://leetcode.com/problems/split-array-with-same-average/description/

In a given integer array A, we must move every element of A to either list B
or list C. (B and C initially start empty.)

Return true if and only if after such a move, it is possible that the average
value of B is equal to the average value of C, and B and C are both non-empty.

    
    
    **Example :**
    **Input:** 
    [1,2,3,4,5,6,7,8]
    **Output:** true
    **Explanation:** We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.
    

**Note:**

  * The length of `A` will be in the range [1, 30].
  * `A[i]` will be in the range of `[0, 10000]`.


Similar Questions:

"""
from fractions import Fraction


class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        N = len(A)
        S = sum(A)
        A = [z - Fraction(S, N) for z in A]

        if N == 1: return False

        # Want zero subset sum
        left = {A[0]}
        for i in range(1, N//2):
            left = {z + A[i] for z in left} | left | {A[i]}
        if 0 in left: return True

        right = {A[-1]}
        for i in range(N//2, N-1):
            right = {z + A[i] for z in right} | right | {A[i]}
        if 0 in right: return True

        sleft = sum(A[:N//2])
        sright = sum(A[N//2:])
        return any((-ha in right and (ha, -ha) != (sleft, sright) for ha in left))


class T(unittest.TestCase):
    def test(self):
        """一般性数据"""
        s = Solution()
        self.assertTrue(s.splitArraySameAverage([1, 2, 3, 4, 5, 6, 7, 8]))
        self.assertTrue(s.splitArraySameAverage([2, 1, 3]))

    def test2(self):
        """整个列表有效的数据"""
        s = Solution()
        self.assertFalse(s.splitArraySameAverage([6, 8, 18, 3, 1]))

    def test3(self):
        """除不尽的数据"""
        s = Solution()
        self.assertTrue(s.splitArraySameAverage([4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5]))

    def test4(self):
        """超时"""
        s = Solution()
        self.assertFalse(s.splitArraySameAverage([71,54,44,61,55,34,42,17,56,16,26,86,97,52,24,48,29,19,15]))
        self.assertFalse(s.splitArraySameAverage(
            [3863, 703, 1799, 327, 3682, 4330, 3388, 6187, 5330, 6572, 938, 6842, 678, 9837, 8256,
             6886, 2204, 5262, 6643, 829, 745, 8755, 3549, 6627, 1633, 4290, 7]))


if __name__ == "__main__":
    unittest.main()
