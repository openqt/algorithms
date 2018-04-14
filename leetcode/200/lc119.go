package main

import "fmt"

/*119. Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/description/

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
*/
func getRow(rowIndex int) []int {
	cur, last := make([]int, rowIndex+1), make([]int, rowIndex+1)
	for i := 0; i <= rowIndex; i++ {
		cur[i] = 1
		last[i] = 1
	}

	for i := 2; i <= rowIndex; i++ {
		for j := 1; j < i; j++ {
			last[j] = cur[j-1] + cur[j]
		}
		cur, last = last, cur
	}
	return cur
}

func main() {
	//2 = [1, 2, 1]
	//3 = [1, 3, 3, 1]
	//4 = [1, 4, 6, 4, 1]
	//5 = [1, 5, 10, 10, 5, 1]
	//6 = [1, 6, 15, 20, 15, 6, 1]
	//7 = [1, 7, 21, 35, 35, 21, 7, 1]
	fmt.Println(getRow(6))
}
