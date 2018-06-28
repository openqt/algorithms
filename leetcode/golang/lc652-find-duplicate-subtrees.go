package main

import (
	"fmt"
)

/*652. Find Duplicate Subtrees
https://leetcode.com/problems/find-duplicate-subtrees/description/

Given a binary tree, return all duplicate subtrees. For each kind of duplicate
subtrees, you only need to return the root node of any **one** of them.

Two trees are duplicate if they have the same structure with same node values.

**Example 1:**

    
    
            1
           / \
          2   3
         /   / \
        4   2   4
           /
          4
    

The following are two duplicate subtrees:

    
    
          2
         /
        4
    

and

    
    
        4
    

Therefore, you need to return above trees' root in the form of a list.


Similar Questions:
  Serialize and Deserialize Binary Tree (serialize-and-deserialize-binary-tree)
  Serialize and Deserialize BST (serialize-and-deserialize-bst)
  Construct String from Binary Tree (construct-string-from-binary-tree)
*/
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findDuplicateSubtrees(root *TreeNode) []*TreeNode {
    
}

func main() {
	fmt.Println()
}
