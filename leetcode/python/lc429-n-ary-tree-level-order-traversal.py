# coding=utf-8
import unittest

"""429. N-ary Tree Level Order Traversal
https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/

Given an n-ary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example, given a `3-ary` tree:



![](/static/images/problemset/NaryTreeExample.png)



We should return its level order traversal:





    
    
    [
         [1],
         [3,2,4],
         [5,6]
    ]
    



**Note:**

  1. The depth of the tree is at most `1000`.
  2. The total number of nodes is at most `5000`.


Similar Questions:
  Binary Tree Level Order Traversal (binary-tree-level-order-traversal)
  N-ary Tree Preorder Traversal (n-ary-tree-preorder-traversal)
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
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
