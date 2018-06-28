# coding=utf-8
import unittest

"""327. Count of Range Sum
https://leetcode.com/problems/count-of-range-sum/description/

Given an integer array `nums`, return the number of range sums that lie in
`[lower, upper]` inclusive.  
Range sum `S(i, j)` is defined as the sum of the elements in `nums` between
indices `i` and `j` (`i` ≤ `j`), inclusive.

**Note:**  
A naive algorithm of _O_ ( _n_ 2) is trivial. You MUST do better than that.

**Example:**

    
    
    **Input:** _nums_ = [-2,5,-1], _lower_ = -2, _upper_ = 2,
    **Output:** 3 
    **Explanation:** The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.


Similar Questions:
  Count of Smaller Numbers After Self (count-of-smaller-numbers-after-self)
  Reverse Pairs (reverse-pairs)
"""


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
