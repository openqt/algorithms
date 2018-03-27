package main

import (
	"fmt"
)

/* 125. Backpack II
http://www.lintcode.com/en/problem/backpack-ii/

Given n items with size Ai and value Vi, and a backpack with size m.
What's the maximum value can you put into the backpack?

Notice
	You cannot divide item into small pieces and the total size of items you choose should smaller or equal to m.

Example
	Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and a backpack with size 10. The maximum value is 9.
*/
/**
 * @param m: An integer m denotes the size of a backpack
 * @param A: Given n items with size A[i]
 * @param V: Given n items with value V[i]
 * @return: The maximum value
 */
func backPackII(m int, A []int, V []int) int {
	book := make([][]int, len(A))
	for i := 0; i < len(book); i++ {
		book[i] = make([]int, m+1)
	}

	for j := A[0]; j <= m; j++ {
		book[0][j] = V[0]
	}

	for i := 1; i < len(book); i++ {
		for j := 0; j <= m; j++ {
			if j < A[i] {
				book[i][j] = book[i-1][j]
			} else {
				book[i][j] = max(book[i-1][j], V[i]+book[i-1][j-A[i]])
			}
		}
	}
	//for n, i := range book {
	//	fmt.Println(A[n], i)
	//}
	return book[len(book)-1][m]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	fmt.Println(backPackII(10, []int{2, 3, 5, 7}, []int{1, 5, 2, 4}) == 9)
}
