# coding=utf-8
import unittest

"""319. Bulb Switcher
https://leetcode.com/problems/bulb-switcher/description/

There are _n_ bulbs that are initially off. You first turn on all the bulbs.
Then, you turn off every second bulb. On the third round, you toggle every
third bulb (turning on if it 's off or turning off if it's on). For the _i_
-th round, you toggle every _i_ bulb. For the _n_ -th round, you only toggle
the last bulb. Find how many bulbs are on after _n_ rounds.

**Example:**

    
    
    **Input:** 3
    **Output:** 1 
    **Explanation:** 
    At first, the three bulbs are **[off, off, off]**.
    After first round, the three bulbs are **[on, on, on]**.
    After second round, the three bulbs are **[on, off, on]**.
    After third round, the three bulbs are **[on, off, off]**. 
    
    So you should return 1, because there is only one bulb is on.


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
