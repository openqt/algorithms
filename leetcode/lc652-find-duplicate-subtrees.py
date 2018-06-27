# coding=utf-8
import unittest

"""Find Duplicate Subtrees
https://leetcode.com/problems/find-duplicate-subtrees/description/

<p>Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any <b>one</b> of them.</p>

<p>Two trees are duplicate if they have the same structure with same node values.</p>

<p><b>Example 1: </b></p>

<pre>
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
</pre>

<p>The following are two duplicate subtrees:</p>

<pre>
      2
     /
    4
</pre>

<p>and</p>

<pre>
    4
</pre>
Therefore, you need to return above trees&#39; root in the form of a list.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
