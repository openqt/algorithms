# coding=utf-8
import unittest

"""590. N-ary Tree Postorder Traversal
https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/

Given an n-ary tree, return the _postorder_ traversal of its nodes ' values.



For example, given a `3-ary` tree:

![](/static/images/problemset/NaryTreeExample.png)



Return its postorder traversal as: `[5,6,3,2,4,1]`.



**Note:** Recursive solution is trivial, could you do it iteratively?


Similar Questions:
  Binary Tree Postorder Traversal (binary-tree-postorder-traversal)
  N-ary Tree Level Order Traversal (n-ary-tree-level-order-traversal)
  N-ary Tree Preorder Traversal (n-ary-tree-preorder-traversal)
"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        output = []
        self._postorder(root, output)
        return output

    def _postorder(self, node, output):
        if node:
            for child in node.children:
                self._postorder(child, output)
            output.append(node.val)



if __name__ == "__main__":
    unittest.main()
