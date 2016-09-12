'''
Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if not root: return 0
        if root.right and root.left: return min(self.minDepth(root.left)+1, self.minDepth(root.right)+1)
        if root.left: return self.minDepth(root.left) + 1
        if root.right: return self.minDepth(root.right) + 1
        return 1


if __name__ == '__main__':
    s = Solution()
    print 'PASS'
