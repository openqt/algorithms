# coding=utf-8
import unittest

"""600. Non-negative Integers without Consecutive Ones
https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/description/

<p>Given a positive integer n, find the number of <b>non-negative</b> integers less than or equal to n, whose binary representations do NOT contain <b>consecutive ones</b>.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 5
<b>Output:</b> 5
<b>Explanation:</b> 
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule. 
</pre>
</p>

<p><b>Note:</b>
1 <= n <= 10<sup>9</sup>
</p>

Similar Questions:
  House Robber (house-robber)
  House Robber II (house-robber-ii)
  Ones and Zeroes (ones-and-zeroes)
"""


class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
