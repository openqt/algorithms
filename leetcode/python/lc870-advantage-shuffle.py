# coding=utf-8
import unittest

"""870. Advantage Shuffle
https://leetcode.com/problems/advantage-shuffle/description/

Given two arrays `A` and `B` of equal size, the _advantage of`A` with respect
to `B`_ is the number of indices `i` for which `A[i] > B[i]`.

Return **any** permutation of `A` that maximizes its advantage with respect to
`B`.



**Example 1:**

    
    
    **Input:** A = [2,7,11,15], B = [1,10,4,11]
    **Output:** [2,11,7,15]
    

**Example 2:**

    
    
    **Input:** A = [12,24,8,32], B = [13,25,32,11]
    **Output:** [24,32,8,12]
    



**Note:**

  1. `1 <= A.length = B.length <= 10000`
  2. `0 <= A[i] <= 10^9`
  3. `0 <= B[i] <= 10^9`


Similar Questions:

"""


class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
