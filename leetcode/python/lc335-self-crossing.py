# coding=utf-8
import unittest

"""335. Self Crossing
https://leetcode.com/problems/self-crossing/description/

You are given an array _x_ of `n` positive numbers. You start at point `(0,0)`
and moves `x[0]` metres to the north, then `x[1]` metres to the west, `x[2]`
metres to the south, `x[3]` metres to the east and so on. In other words,
after each move your direction changes counter-clockwise.

Write a one-pass algorithm with `O(1)` extra space to determine, if your path
crosses itself, or not.

**Example 1:**  

    
    
    Given _x_ = [2, 1, 1, 2],
    ?????
    ?   ?
    ???????>
        ?
    
    Return **true** (self crossing)
    

**Example 2:**  

    
    
    Given _x_ = [1, 2, 3, 4],
    ????????
    ?      ?
    ?
    ?
    ?????????????>
    
    Return **false** (not self crossing)
    

**Example 3:**  

    
    
    Given _x_ = [1, 1, 1, 1],
    ?????
    ?   ?
    ?????>
    
    Return **true** (self crossing)
    

**Credits:**  
Special thanks to [@dietpepsi](https://leetcode.com/discuss/user/dietpepsi)
for adding this problem and creating all test cases.


Similar Questions:

"""


class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
