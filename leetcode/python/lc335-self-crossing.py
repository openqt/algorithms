# coding=utf-8
import unittest

"""335. Self Crossing
https://leetcode.com/problems/self-crossing/description/

<p>
    You are given an array <i>x</i> of <code>n</code> positive numbers. You start at point <code>(0,0)</code> and moves <code>x[0]</code> metres to the north, then <code>x[1]</code> metres to the west,
    <code>x[2]</code> metres to the south,
    <code>x[3]</code> metres to the east and so on. In other words, after each move your direction changes
    counter-clockwise.
</p>
<p>
    Write a one-pass algorithm with <code>O(1)</code> extra space to determine, if your path crosses itself, or not.
</p>

<p>
<b>Example 1:</b><br/>
<pre>
Given <i>x</i> = <code>[2, 1, 1, 2]</code>,
?????
?   ?
???????>
    ?

Return <b>true</b> (self crossing)
</pre>
</p>

<p>
<b>Example 2:</b><br/>
<pre>
Given <i>x</i> = <code>[1, 2, 3, 4]</code>,
????????
?      ?
?
?
?????????????>

Return <b>false</b> (not self crossing)
</pre>
</p>

<p>
<b>Example 3:</b><br/>
<pre>
Given <i>x</i> = <code>[1, 1, 1, 1]</code>,
?????
?   ?
?????>

Return <b>true</b> (self crossing)
</pre>
</p>

<p><b>Credits:</b><br />Special thanks to <a href="https://leetcode.com/discuss/user/dietpepsi">@dietpepsi</a> for adding this problem and creating all test cases.</p>
Similar Questions:

"""


class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
