# coding=utf-8
import unittest

"""Number of Boomerangs
https://leetcode.com/problems/number-of-boomerangs/description/

<p>Given <i>n</i> points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points <code>(i, j, k)</code> such that the distance between <code>i</code> and <code>j</code> equals the distance between <code>i</code> and <code>k</code> (<b>the order of the tuple matters</b>).</p>

<p>Find the number of boomerangs. You may assume that <i>n</i> will be at most <b>500</b> and coordinates of points are all in the range <b>[-10000, 10000]</b> (inclusive).</p>

<p><b>Example:</b><br />
<pre>
<b>Input:</b>
[[0,0],[1,0],[2,0]]

<b>Output:</b>
2

<b>Explanation:</b>
The two boomerangs are <b>[[1,0],[0,0],[2,0]]</b> and <b>[[1,0],[2,0],[0,0]]</b>
</pre>
</p>
"""


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
