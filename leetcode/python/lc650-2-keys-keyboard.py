# coding=utf-8
import unittest

"""650. 2 Keys Keyboard
https://leetcode.com/problems/2-keys-keyboard/description/

<p>
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step: 
<ol>
<li><code>Copy All</code>: You can copy all the characters present on the notepad (partial copy is not allowed).</li>
<li><code>Paste</code>: You can paste the characters which are copied <b>last time</b>.</li>
</ol>
</p>

<p>
Given a number <code>n</code>. You have to get <b>exactly</b> <code>n</code> 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get <code>n</code> 'A'. 
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 3
<b>Output:</b> 3
<b>Explanation:</b>
Intitally, we have one character 'A'.
In step 1, we use <b>Copy All</b> operation.
In step 2, we use <b>Paste</b> operation to get 'AA'.
In step 3, we use <b>Paste</b> operation to get 'AAA'.
</pre>
</p>


<p><b>Note:</b><br>
<ol>
<li>The <code>n</code> will be in the range [1, 1000].</li>
</ol>
</p>
Similar Questions:
  4 Keys Keyboard (4-keys-keyboard)
"""


class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
