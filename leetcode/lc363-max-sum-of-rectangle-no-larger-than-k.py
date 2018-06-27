# coding=utf-8
import unittest

"""Max Sum of Rectangle No Larger Than K
https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/

<p>Given a non-empty 2D matrix <i>matrix</i> and an integer <i>k</i>, find the max sum of a rectangle in the <i>matrix</i> such that its sum is no larger than <i>k</i>.</p>

<p><b>Example:</b><br />
<pre>Given matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2
</pre>
</p>

<p>The answer is <code>2</code>. Because the sum of rectangle <code>[[0, 1], [-2, 3]]</code> is 2 and 2 is the max number no larger than k (k = 2).</p>

<p><b>Note:</b><br />
<ol>
<li>The rectangle inside the matrix must have an area > 0.</li>
<li>What if the number of rows is much larger than the number of columns?</li>
</ol>
</p>

<p><b>Credits:</b><br />Special thanks to <a href="https://discuss.leetcode.com/user/fujiaozhu">@fujiaozhu</a> for adding this problem and creating all test cases.</p>
"""


class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
