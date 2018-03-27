package main

import (
	"fmt"
)

/* 92. Backpack
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
	return 0
}

// http://www.code123.cc/docs/leetcode-notes/dynamic_programming/backpack.html
func main() {
	fmt.Println(backPack(11, []int{2, 3, 5, 7}) == 10)
	fmt.Println(backPack(12, []int{2, 3, 5, 7}) == 12)
}
