# coding=utf-8
import unittest

"""589. N-ary Tree Preorder Traversal
https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/

Given an n-ary tree, return the _preorder_ traversal of its nodes ' values.



For example, given a `3-ary` tree:

![](/static/images/problemset/NaryTreeExample.png)



Return its preorder traversal as: `[1,3,5,6,2,4]`.



**Note:** Recursive solution is trivial, could you do it iteratively?


Similar Questions:
  Binary Tree Preorder Traversal (binary-tree-preorder-traversal)
  N-ary Tree Level Order Traversal (n-ary-tree-level-order-traversal)
  N-ary Tree Postorder Traversal (n-ary-tree-postorder-traversal)
"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
