# coding=utf-8
import unittest

"""Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/description/

<p>Given <em>n</em> points on a 2D plane, find the maximum number of points that lie on the same straight line.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [[1,1],[2,2],[3,3]]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
^
|
| &nbsp; &nbsp; &nbsp; &nbsp;o
| &nbsp; &nbsp; o
| &nbsp;o &nbsp;
+-------------&gt;
0 &nbsp;1 &nbsp;2 &nbsp;3  4
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
<strong>Output:</strong> 4
<strong>Explanation:</strong>
^
|
|  o
| &nbsp;&nbsp;&nbsp;&nbsp;o&nbsp;&nbsp;      o
| &nbsp;&nbsp;&nbsp;&nbsp;   o
| &nbsp;o &nbsp;      o
+-------------------&gt;
0 &nbsp;1 &nbsp;2 &nbsp;3 &nbsp;4 &nbsp;5 &nbsp;6
</pre>

"""


# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
