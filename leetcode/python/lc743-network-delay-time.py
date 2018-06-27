# coding=utf-8
import unittest

"""743. Network Delay Time
https://leetcode.com/problems/network-delay-time/description/

<p>
There are <code>N</code> network nodes, labelled <code>1</code> to <code>N</code>.
</p><p>
Given <code>times</code>, a list of travel times as <b>directed</b> edges <code>times[i] = (u, v, w)</code>, where <code>u</code> is the source node, <code>v</code> is the target node, and <code>w</code> is the time it takes for a signal to travel from source to target.
</p><p>
Now, we send a signal from a certain node <code>K</code>.  How long will it take for all nodes to receive the signal?  If it is impossible, return <code>-1</code>.
</p>

<p><b>Note:</b><br>
<ol>
<li><code>N</code> will be in the range <code>[1, 100]</code>.</li>
<li><code>K</code> will be in the range <code>[1, N]</code>.</li>
<li>The length of <code>times</code> will be in the range <code>[1, 6000]</code>.</li>
<li>All edges <code>times[i] = (u, v, w)</code> will have <code>1 <= u, v <= N</code> and <code>1 <= w <= 100</code>.</li>
</ol>
</p>
"""


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
