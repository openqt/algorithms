package main

import (
	"fmt"
)

/* 92. Backpack
http://www.lintcode.com/en/problem/backpack/

Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?

Notice
	You can not divide any item into small pieces.

Example
	If we have 4 items with size [2, 3, 5, 7], the backpack size is 11,
	we can select [2, 3, 5], so that the max size we can fill this backpack is 10.
	If the backpack size is 12. we can select [2, 3, 7] so that we can fulfill the backpack.

	You function should return the max size we can fill in the given backpack.
*/
/**
 * @param m: An integer m denotes the size of a backpack
 * @param A: Given n items with size A[i]
 * @return: The maximum size
 */
func backPack(m int, A []int) int {
	book := make([][]int, len(A))
	for i := 0; i < len(book); i++ {
		book[i] = make([]int, m+1)
	}

	for j := A[0]; j <= m; j++ {
		book[0][j] = A[0]
	}

	for i := 1; i < len(book); i++ {
		for j := 0; j <= m; j++ {
			if j < A[i] {
				book[i][j] = book[i-1][j]
			} else {
				book[i][j] = max(book[i-1][j], A[i]+book[i-1][j-A[i]])
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

// http://www.code123.cc/docs/leetcode-notes/dynamic_programming/backpack.html
func main() {
	fmt.Println(backPack(11, []int{2, 3, 5, 7}) == 10)
	fmt.Println(backPack(12, []int{2, 3, 5, 7}) == 12)
	fmt.Println(backPack(10, []int{20,15,15,15,15,15,7,2,15,15,15,15}) == 9)
	fmt.Println(backPack(10, []int{20,15,15,15,15,15,15,15,15,15,15,15,15,15,15,7,2,15,15,15,15}) == 9)
}
