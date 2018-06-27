package main

/*766. Toeplitz Matrix
https://leetcode.com/problems/toeplitz-matrix/description/

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

Example 1:
	Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
	Output: True
	Explanation:
		1234
		5123
		9512
	In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]",
	and in each diagonal all elements are the same, so the answer is True.

Example 2:
	Input: matrix = [[1,2],[2,2]]
	Output: False
	Explanation:
	The diagonal "[1, 2]" has different elements.

Note:
	matrix will be a 2D array of integers.
	matrix will have a number of rows and columns in range [1, 20].
	matrix[i][j] will be integers in range [0, 99].
*/
func isToeplitzMatrix(matrix [][]int) bool {
	if len(matrix) == 0 {
		return false
	}
	size := len(matrix[0])
	for i := 1; i < len(matrix); i++ {
		if !cmp(matrix[i-1][:size-1], matrix[i][1:]) {
			return false
		}
	}
	return true
}

func cmp(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for n, i := range a {
		if b[n] != i {
			return false
		}
	}
	return true
}

func main() {
}
