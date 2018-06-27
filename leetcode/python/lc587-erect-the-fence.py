# coding=utf-8
import unittest

"""587. Erect the Fence
https://leetcode.com/problems/erect-the-fence/description/

<p>There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden. Your job is to fence the entire garden using the <b>minimum length</b> of rope as it is expensive. The garden is well fenced only if all the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
<b>Output:</b> [[1,1],[2,0],[4,2],[3,3],[2,4]]
<b>Explanation:</b>
<img src="/static/images/problemset/erect_the_fence_1.png" width = "30%" />
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [[1,2],[2,2],[4,2]]
<b>Output:</b> [[1,2],[2,2],[4,2]]
<b>Explanation:</b>
<img src="/static/images/problemset/erect_the_fence_2.png" width = "30%" />
Even you only have trees in a line, you need to use rope to enclose them. 
</pre>
</p>

<p> Note: 
<ol>
<li>All trees should be enclosed together. You cannot cut the rope to enclose trees that will separate them in more than one group.</li>
<li>All input integers will range from 0 to 100. </li>
<li>The garden has at least one tree. </li>
<li>All coordinates are distinct. </li>
<li>Input points have <b>NO</b> order. No order required for output.</li>
</ol>
</p>
Similar Questions:

"""


# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
