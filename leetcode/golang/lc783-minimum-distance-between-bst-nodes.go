package main

import (
	"fmt"
)

/*783. Minimum Distance Between BST Nodes
https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/

<p>Given a Binary Search Tree (BST) with the root node <code>root</code>, return&nbsp;the minimum difference between the values of any two different nodes in the tree.</p>

<p><strong>Example :</strong></p>

<pre>
<strong>Input:</strong> root = [4,2,6,1,3,null,null]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li>The size of the BST will be between 2 and&nbsp;<code>100</code>.</li>
	<li>The BST is always valid, each node&#39;s value is an integer, and each node&#39;s value is different.</li>
</ol>
Similar Questions:
  Binary Tree Inorder Traversal (binary-tree-inorder-traversal)
*/
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func minDiffInBST(root *TreeNode) int {
    
}

func main() {
	fmt.Println()
}
