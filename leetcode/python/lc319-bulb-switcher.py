# coding=utf-8
import unittest

"""319. Bulb Switcher
https://leetcode.com/problems/bulb-switcher/description/

<p>There are <i>n</i> bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it&#39;s off or turning off if it&#39;s on). For the <i>i</i>-th round, you toggle every <i>i</i> bulb. For the <i>n</i>-th round, you only toggle the last bulb. Find how many bulbs are on after <i>n</i> rounds.</p>

<p><b>Example:</b></p>

<pre>
<strong>Input: </strong>3
<strong>Output:</strong> 1 
<strong>Explanation:</strong> 
At first, the three bulbs are <b>[off, off, off]</b>.
After first round, the three bulbs are <b>[on, on, on]</b>.
After second round, the three bulbs are <b>[on, off, on]</b>.
After third round, the three bulbs are <b>[on, off, off]</b>. 

So you should return 1, because there is only one bulb is on.
</pre>

Similar Questions:
  Bulb Switcher II (bulb-switcher-ii)
"""


class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
