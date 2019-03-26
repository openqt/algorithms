# coding=utf-8
import unittest

"""559. Maximum Depth of N-ary Tree
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

For example, given a `3-ary` tree:



![](/static/images/problemset/NaryTreeExample.png)



We should return its max depth, which is 3.

**Note:**

  1. The depth of the tree is at most `1000`.
  2. The total number of nodes is at most `5000`.


Similar Questions:
  Maximum Depth of Binary Tree (maximum-depth-of-binary-tree)
"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root:
            if root.children:
                return max(self.maxDepth(i) for i in root.children) + 1
            return 1
        return 0


if __name__ == "__main__":
    unittest.main()
