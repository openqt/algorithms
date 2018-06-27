package main

import (
	"fmt"
)

/*671. Second Minimum Node In a Binary Tree
https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/

<p>
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly <code>two</code> or <code>zero</code> sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. 
</p>

<p>
Given such a binary tree, you need to output the <b>second minimum</b> value in the set made of all the nodes' value in the whole tree. 
</p>

<p>
If no such second minimum value exists, output -1 instead.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
    2
   / \
  2   5
     / \
    5   7

<b>Output:</b> 5
<b>Explanation:</b> The smallest value is 2, the second smallest value is 5.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
    2
   / \
  2   2

<b>Output:</b> -1
<b>Explanation:</b> The smallest value is 2, but there isn't any second smallest value.
</pre>
</p>
Similar Questions:
  Kth Smallest Element in a BST (kth-smallest-element-in-a-bst)
*/
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findSecondMinimumValue(root *TreeNode) int {
    
}

func main() {
	fmt.Println()
}
