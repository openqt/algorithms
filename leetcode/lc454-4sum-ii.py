# coding=utf-8
import unittest

"""4Sum II
https://leetcode.com/problems/4sum-ii/description/

<p>Given four lists A, B, C, D of integer values, compute how many tuples <code>(i, j, k, l)</code> there are such that <code>A[i] + B[j] + C[k] + D[l]</code> is zero.</p>

<p>To make problem a bit easier, all A, B, C, D have same length of N where 0 &le; N &le; 500. All integers are in the range of -2<sup>28</sup> to 2<sup>28</sup> - 1 and the result is guaranteed to be at most 2<sup>31</sup> - 1.</p>

<p><b>Example:</b>
<pre>
<b>Input:</b>
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

<b>Output:</b>
2

<b>Explanation:</b>
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
</pre>
</p>
"""


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
