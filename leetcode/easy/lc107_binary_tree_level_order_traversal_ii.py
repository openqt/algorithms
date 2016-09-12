'''
Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
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
    def levelOrderBottom(self, root):
        if not root: return []

        Q = [root]
        val = []
        while Q:
            val.append([i.val for i in Q])
            q = Q; Q = []
            for i in q:
                if i.left: Q.append(i.left)
                if i.right: Q.append(i.right)
        return val[::-1]


if __name__ == '__main__':
    s = Solution()
    print 'PASS'
