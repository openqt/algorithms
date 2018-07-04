package main

import (
	"fmt"
)

/* 73. Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/description/

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

Follow up:
	Did you use extra space?
	A straight forward solution using O(mn) space is probably a bad idea.
	A simple improvement uses O(m + n) space, but still not the best solution.
	Could you devise a constant space solution?
*/
func setZeroes(matrix [][]int) {
	// 最简单的mark位置，就是第一行第一列。
	// 用第一行来保存各个列的mark，用第一列来保存各个行的mark。
	row0 := false
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			if matrix[i][j] == 0 {
				if i == 0 {
					row0 = true
				} else {
					matrix[i][0] = 0
				}
				matrix[0][j] = 0
			}
		}
	}

	for i := 1; i < len(matrix); i++ {
		if matrix[i][0] == 0 {
			setRow(matrix, i)
		}
	}
	for j := 1; j < len(matrix[0]); j++ {
		if matrix[0][j] == 0 {
			setCol(matrix, j)
		}
	}

	if matrix[0][0] == 0 {
		setCol(matrix, 0)
	}
	if row0 {
		setRow(matrix, 0)
	}
}

func setRow(matrix [][]int, n int) {
	for j := 0; j < len(matrix[0]); j++ {
		matrix[n][j] = 0
	}
}

func setCol(matrix [][]int, n int) {
	for i := 0; i < len(matrix); i++ {
		matrix[i][n] = 0
	}
}

// http://www.cnblogs.com/lupx/p/leetcode-73.html
func main() {
	m := [][]int{
		{1, 3, 0, 4},
		{1, 9, 7, 4},
		{1, 2, 0, 4},
		{0, 3, 0, 1},
	}
	setZeroes(m)

	for _, i := range m {
		fmt.Println(i)
	}
}
