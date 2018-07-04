package main

import "fmt"

/*257. Binary Tree Paths
https://leetcode.com/problems/binary-tree-paths/description/

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

*/
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func binaryTreePaths(root *TreeNode) []string {
	var paths []string
	if root != nil {
		treePaths(root, fmt.Sprintf("%v", root.Val), &paths)
	}
	return paths
}

func treePaths(root *TreeNode, path string, paths *[]string) {
	if root.Left != nil {
		treePaths(root.Left, fmt.Sprintf("%v->%v", path, root.Left.Val), paths)
	}
	if root.Right != nil {
		treePaths(root.Right, fmt.Sprintf("%v->%v", path, root.Right.Val), paths)
	}
	if root.Left == nil && root.Right == nil {
		*paths = append(*paths, path)
	}
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {
	tree := TreeNode{Val: 1, Left: &TreeNode{Val: 2, Right: &TreeNode{Val: 5}}, Right: &TreeNode{Val: 3}}
	fmt.Println(binaryTreePaths(&tree))
}
