package main

import (
	"fmt"
)

/* 556. Next Greater Element III
https://leetcode.com/problems/next-greater-element-iii/description/

Given a positive 32-bit integer n, you need to find the smallest 32-bit integer
which has exactly the same digits existing in the integer n and is greater in value than n.
If no such positive 32-bit integer exists, you need to return -1.

Example 1:

	Input: 12
	Output: 21


Example 2:

	Input: 21
	Output: -1
*/
func nextGreaterElement(n int) int {
	nums := slice(n)
	for nextPermutation(nums) {
		val := merge(nums)
		if val > n && val <= 2147483647 {
			return val
		}
	}
	return -1
}

func nextPermutation(nums []int) bool {
	// find non-reverse-order
	pos := len(nums) - 2
	for ; pos >= 0; pos-- {
		if nums[pos+1] > nums[pos] {
			break
		}
	}
	if pos < 0 {
		return false
	}

	// swap with the second smaller
	for i := len(nums) - 1; i > pos; i-- {
		if nums[i] > nums[pos] {
			nums[i], nums[pos] = nums[pos], nums[i]
			break
		}
	}
	// reverse
	reverse(nums, pos+1, len(nums)-1)
	return true
}

func reverse(nums []int, a, b int) {
	for a < b {
		nums[a], nums[b] = nums[b], nums[a]
		a++
		b--
	}
}

func slice(n int) []int {
	var nums []int
	for ; n > 0; n /= 10 {
		nums = append(nums, n%10)
	}
	reverse(nums, 0, len(nums)-1)
	return nums
}

func merge(nums []int) int {
	n := 0
	for _, i := range nums {
		n = n*10 + i
	}
	return n
}

func main() {
	//m := []int{3, 4, 5}
	//for i := 0; i < 10; i++ {
	//	nextPermutation(m)
	//}
	fmt.Println(nextGreaterElement(12) == 21)
	fmt.Println(nextGreaterElement(21) == -1)
	fmt.Println(nextGreaterElement(1999999999) == -1)
	fmt.Println(nextGreaterElement(101) == 110)
	fmt.Println(nextGreaterElement(198765432) == 213456789)
}
