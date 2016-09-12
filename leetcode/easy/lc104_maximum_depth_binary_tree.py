'''
Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
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
    def maxDepth(self, root):
        if root is None: return 0

        Q = [root]
        depth = 0
        while Q:
            depth += 1
            q = Q; Q = []
            for node in q:
                if node.left: Q.append(node.left)
                if node.right: Q.append(node.right)
        return depth

    def maxDepth2(self, root):
        if root is None: return 0
        lh = self.maxDepth(root.left) + 1
        rh = self.maxDepth(root.right) + 1
        return max(lh, rh)


if __name__ == '__main__':
    from utils import TreeNode

    s = Solution()

    head = TreeNode.toTreeNode('1234567')
    print s.maxDepth(head)
    print s.maxDepth2(head)
    print 'PASS'
