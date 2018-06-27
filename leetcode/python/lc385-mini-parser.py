# coding=utf-8
import unittest

"""385. Mini Parser
https://leetcode.com/problems/mini-parser/description/

<p>Given a nested list of integers represented as a string, implement a parser to deserialize it.</p>

<p>Each element is either an integer, or a list -- whose elements may also be integers or other lists.</p>

<p><b>Note:</b>
You may assume that the string is well-formed:
<ul>
<li>String is non-empty.</li>
<li>String does not contain white spaces.</li>
<li>String contains only digits <code>0-9</code>, <code>[</code>, <code>-</code> <code>,</code>, <code>]</code>.</li>
</ul>
</p>

<p><b>Example 1:</b>
<pre>
Given s = "324",

You should return a NestedInteger object which contains a single integer 324.
</pre>
</p>

<p><b>Example 2:</b>
<pre>
Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.
</pre>
</p>
Similar Questions:
  Flatten Nested List Iterator (flatten-nested-list-iterator)
  Ternary Expression Parser (ternary-expression-parser)
  Remove Comments (remove-comments)
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
