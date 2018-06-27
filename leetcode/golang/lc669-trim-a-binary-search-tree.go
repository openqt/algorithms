package main

import (
	"fmt"
)

/*669. Trim a Binary Search Tree
https://leetcode.com/problems/trim-a-binary-search-tree/description/

<p>
Given a binary search tree and the lowest and highest boundaries as <code>L</code> and <code>R</code>, trim the tree so that all its elements lies in <code>[L, R]</code> (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
    1
   / \
  0   2

  L = 1
  R = 2

<b>Output:</b> 
    1
      \
       2
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

<b>Output:</b> 
      3
     / 
   2   
  /
 1
</pre>
</p>
Similar Questions:

*/
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func trimBST(root *TreeNode, L int, R int) *TreeNode {
    
}

func main() {
	fmt.Println()
}
