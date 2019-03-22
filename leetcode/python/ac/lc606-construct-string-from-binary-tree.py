# coding=utf-8
import unittest

"""606. Construct String from Binary Tree
https://leetcode.com/problems/construct-string-from-binary-tree/description/

You need to construct a string consists of parenthesis and integers from a
binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you
need to omit all the empty parenthesis pairs that don't affect the one-to-one
mapping relationship between the string and the original binary tree.

**Example 1:**  

    
    
    **Input:** Binary tree: [1,2,3,4]
           1
         /   \
        2     3
       /    
      4     
    
    **Output:** "1(2(4))(3)"
      
    **Explanation:** Originallay it needs to be "1(2(4)())(3()())",   
     but you need to omit all the unnecessary empty parenthesis pairs.   
    And it will be "1(2(4))(3)".
    

**Example 2:**  

    
    
    **Input:** Binary tree: [1,2,3,null,4]
           1
         /   \
        2     3
         \  
          4 
    
    **Output:** "1(2()(4))(3)"
      
    **Explanation:** Almost the same as the first example,   
     except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.


Similar Questions:
  Construct Binary Tree from String (construct-binary-tree-from-string)
  Find Duplicate Subtrees (find-duplicate-subtrees)
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        self.s = ""
        self._dfs(t)
        return self.s

    def _dfs(self, node):
        if not node: return
        self.s += str(node.val)
        if node.left:
            self.s += '('
            self._dfs(node.left)
            self.s += ')'

        if node.right:
            if node.left:
                self.s += '('
            else:
                self.s += '()('
            self._dfs(node.right)
            self.s += ')'


import tree
class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.tree2str(tree.BinaryTree("1234").root), "1(2(4))(3)")
        self.assertEqual(s.tree2str(tree.BinaryTree("123#4").root), "1(2()(4))(3)")


if __name__ == "__main__":
    unittest.main()
