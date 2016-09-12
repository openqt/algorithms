'''
Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

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
    # @return {boolean}
    def isSymmetric(self, root):
        if not root: return True
        return self._symmetric(root.left, root.right)

    def _symmetric(self, p, q):
        if (p and q) and (p.val == q.val):
            return self._symmetric(p.left, q.right) and self._symmetric(p.right, q.left)
        return p == q


if __name__ == '__main__':
    s = Solution()
    print 'PASS'
