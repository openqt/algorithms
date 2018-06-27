package main

import (
	"fmt"
)

/*617. Merge Two Binary Trees
https://leetcode.com/problems/merge-two-binary-trees/description/

<p>
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. 
</p>
<p>
You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
</p>


<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
<b>Output:</b> 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
</pre>
</p>


<p><b>Note:</b>
The merging process must start from the root nodes of both trees.
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
func mergeTrees(t1 *TreeNode, t2 *TreeNode) *TreeNode {
    
}

func main() {
	fmt.Println()
}
