# coding=utf-8
import unittest

"""Find Mode in Binary Search Tree
https://leetcode.com/problems/find-mode-in-binary-search-tree/description/

<p>Given a binary search tree (BST) with duplicates, find all the <a href="https://en.wikipedia.org/wiki/Mode_(statistics)" target="_blank">mode(s)</a> (the most frequently occurred element) in the given BST.</p>

<p>
Assume a BST is defined as follows:
<ul>
<li>The left subtree of a node contains only nodes with keys <b>less than or equal to</b> the node's key.</li>
<li>The right subtree of a node contains only nodes with keys <b>greater than or equal to</b> the node's key.</li>
<li>Both the left and right subtrees must also be binary search trees.</li>
</ul>
</p>

<p>
For example:<br />
Given BST <code>[1,null,2,2]</code>,<br />
<pre>
   1
    \
     2
    /
   2
</pre>
</p>
<p>
return <code>[2]</code>.
</p>

<p><b>Note:</b>
If a tree has more than one mode, you can return them in any order.
</p>

<p><b>Follow up:</b>
Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
</p>
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
