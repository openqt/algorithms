package main

import (
	"fmt"
)

/*377. Combination Sum IV
https://leetcode.com/problems/combination-sum-iv/description/

Given an integer array with all positive numbers and no duplicates,
find the number of possible combinations that add up to a positive integer target.

Example:

	nums = [1, 2, 3]
	target = 4

	The possible combination ways are:
	(1, 1, 1, 1)
	(1, 1, 2)
	(1, 2, 1)
	(1, 3)
	(2, 1, 1)
	(2, 2)
	(3, 1)

	Note that different sequences are counted as different combinations.
	Therefore the output is 7.

Follow up:
	What if negative numbers are allowed in the given array?
	How does it change the problem?
	What limitation we need to add to the question to allow negative numbers?
*/
func combinationSum4(nums []int, target int) int {
	book := make([]int, target+1)
	book[0] =1
	for i := 1; i < len(book); i++ {
		for _, j := range nums {
			if j <= i {
				book[i] += book[i-j]
			}
		}
	}

	//fmt.Println(book)
	return book[target]
}

//func find(nums []int, target int) int {
//	if target == 0 {
//		return 1
//	} else if target < 0 {
//		return 0
//	}
//
//	total := 0
//	for _, i := range nums {
//		total += find(nums, target-i)
//	}
//	return total
//}

func main() {
	fmt.Println(combinationSum4([]int{1, 2, 3}, 4) == 7)
	fmt.Println(combinationSum4([]int{1, 2, 3}, 32) == 181997601)
}
