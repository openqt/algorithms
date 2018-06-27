# coding=utf-8
import unittest

"""Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/description/

<p>
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
</p>

<p><b>Note:</b><br />
<ol>
<li>You may assume the interval's end point is always bigger than its start point.</li>
<li>Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.</li>
</ol>
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [ [1,2], [2,3], [3,4], [1,3] ]

<b>Output:</b> 1

<b>Explanation:</b> [1,3] can be removed and the rest of intervals are non-overlapping.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [ [1,2], [1,2], [1,2] ]

<b>Output:</b> 2

<b>Explanation:</b> You need to remove two [1,2] to make the rest of intervals non-overlapping.
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
<b>Input:</b> [ [1,2], [2,3] ]

<b>Output:</b> 0

<b>Explanation:</b> You don't need to remove any of the intervals since they're already non-overlapping.
</pre>
</p>
"""


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
