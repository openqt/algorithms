# coding=utf-8
import unittest

"""654. Maximum Binary Tree
https://leetcode.com/problems/maximum-binary-tree/description/

Given an integer array with no duplicates. A maximum tree building on this
array is defined as follow:

  1. The root is the maximum number in the array. 
  2. The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
  3. The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

Construct the maximum tree by the given array and output the root node of this
tree.

**Example 1:**  

    
    
    **Input:** [3,2,1,6,0,5]
    **Output:** return the tree root node representing the following tree:
    
          6
        /   \
       3     5
        \    / 
         2  0   
           \
            1
    

**Note:**  

  1. The size of the given array will be in the range [1,1000].


Similar Questions:

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
