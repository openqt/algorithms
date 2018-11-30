# coding=utf-8
import unittest

"""894. All Possible Full Binary Trees
https://leetcode.com/problems/all-possible-full-binary-trees/description/

A _full binary tree_  is a binary tree where each node has exactly 0 or 2
children.

Return a list of all possible full binary trees with `N` nodes.  Each element
of the answer is the root node of one possible tree.

Each `node` of each tree in the answer **must** have `node.val = 0`.

You may return the final list of trees in any order.



**Example 1:**

    
    
    **Input:** 7
    **Output:** [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
    **Explanation:**
    ![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/22/fivetrees.png)
    



**Note:**

  * `1 <= N <= 20`


Similar Questions:

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
