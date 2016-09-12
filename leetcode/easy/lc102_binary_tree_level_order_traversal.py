'''
Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        if not root: return []

        Q = [root]
        val = []
        while Q:
            val.append([i.val for i in Q])
            q = Q; Q = []
            for i in q:
                if i.left: Q.append(i.left)
                if i.right: Q.append(i.right)
        return val


if __name__ == '__main__':
    from TreeNode import *

    s = Solution()

    head = toTreeNode([])
    print s.levelOrder([])

    head = toTreeNode('123456734567345673456734567345673456789')
    print s.levelOrder(head)

    head = toTreeNode([3,9,20,'#','#',15,7])
    print s.levelOrder(head)

    print 'PASS'
