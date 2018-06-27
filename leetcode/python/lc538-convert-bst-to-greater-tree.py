# coding=utf-8
import unittest

"""538. Convert BST to Greater Tree
https://leetcode.com/problems/convert-bst-to-greater-tree/description/

<p>Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.</p>

<p>
<b>Example:</b>
<pre>
<b>Input:</b> The root of a Binary Search Tree like this:
              5
            /   \
           2     13

<b>Output:</b> The root of a Greater Tree like this:
             18
            /   \
          20     13
</pre>
</p>
Similar Questions:

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
