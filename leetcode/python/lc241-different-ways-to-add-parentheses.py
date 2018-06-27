# coding=utf-8
import unittest

"""241. Different Ways to Add Parentheses
https://leetcode.com/problems/different-ways-to-add-parentheses/description/

<p>Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are <code>+</code>, <code>-</code> and <code>*</code>.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <code>&quot;2-1-1&quot;</code>
<b>Output:</b> <code>[0, 2]</code>
<strong>Explanation: </strong>
((2-1)-1) = 0 
(2-(1-1)) = 2</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input: </b><code>&quot;2*3-4*5&quot;</code>
<b>Output:</b> <code>[-34, -14, -10, -10, 10]</code>
<strong>Explanation: 
</strong>(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10<strong>
</strong></pre>

Similar Questions:
  Unique Binary Search Trees II (unique-binary-search-trees-ii)
  Basic Calculator (basic-calculator)
  Expression Add Operators (expression-add-operators)
"""


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
