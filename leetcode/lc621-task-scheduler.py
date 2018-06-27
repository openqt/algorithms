# coding=utf-8
import unittest

"""Task Scheduler
https://leetcode.com/problems/task-scheduler/description/

<p>Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.</p>

<p>However, there is a non-negative cooling interval <b>n</b> that means between two <b>same tasks</b>, there must be at least n intervals that CPU are doing different tasks or just be idle. </p>

<p>You need to return the <b>least</b> number of intervals the CPU will take to finish all the given tasks.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> tasks = ["A","A","A","B","B","B"], n = 2
<b>Output:</b> 8
<b>Explanation:</b> A -> B -> idle -> A -> B -> idle -> A -> B.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The number of tasks is in the range [1, 10000].</li>
<li>The integer n is in the range [0, 100].</li>
</ol>
</p>
"""


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
