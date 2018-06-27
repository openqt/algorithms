# coding=utf-8
import unittest

"""Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/description/

<p>
Given two non-empty binary trees <b>s</b> and <b>t</b>, check whether tree <b>t</b> has exactly the same structure and node values with a subtree of <b>s</b>. A subtree of <b>s</b> is a tree consists of a node in <b>s</b> and all of this node's descendants. The tree <b>s</b> could also be considered as a subtree of itself.
</p>

<p><b>Example 1:</b><br>

Given tree s:
<pre>
     3
    / \
   4   5
  / \
 1   2
</pre>
Given tree t:
<pre>
   4 
  / \
 1   2
</pre>
Return <b>true</b>, because t has the same structure and node values with a subtree of s.
</p>

<p><b>Example 2:</b><br>

Given tree s:
<pre>
     3
    / \
   4   5
  / \
 1   2
    /
   0
</pre>
Given tree t:
<pre>
   4
  / \
 1   2
</pre>
Return <b>false</b>.
</p>
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
