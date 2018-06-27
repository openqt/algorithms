# coding=utf-8
import unittest

"""687. Longest Univalue Path
https://leetcode.com/problems/longest-univalue-path/description/

<p>Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.</p>

<p><b>Note:</b> The length of path between two nodes is represented by the number of edges between them.</p>

<p>
<b>Example 1:</b>
</p>


<p>
Input:
<pre>
              5
             / \
            4   5
           / \   \
          1   1   5
</pre>
</p>

<p>
Output:
<pre>
2
</pre>
</p>

<p>
<b>Example 2:</b>
</p>


<p>
Input:
<pre>
              1
             / \
            4   5
           / \   \
          4   4   5
</pre>
</p>

<p>
Output:
<pre>
2
</pre>
</p>

<p><b>Note:</b>
The given binary tree has not more than 10000 nodes.  The height of the tree is not more than 1000.
</p>
Similar Questions:
  Binary Tree Maximum Path Sum (binary-tree-maximum-path-sum)
  Count Univalue Subtrees (count-univalue-subtrees)
  Path Sum III (path-sum-iii)
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
