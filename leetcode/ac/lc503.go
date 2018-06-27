package main

import (
	"fmt"
)

/* 503. Next Greater Element II
https://leetcode.com/problems/next-greater-element-ii/description/

Given a circular array (the next element of the last element is the first element of the array),
print the Next Greater Number for every element.
The Next Greater Number of a number x is the first greater number to its traversing-order next in the array,
which means you could search circularly to find its next greater number.
If it doesn't exist, output -1 for this number.

Example 1:
	Input: [1,2,1]
	Output: [2,-1,2]
	Explanation: The first 1's next greater number is 2;
	The number 2 can't find next greater number;
	The second 1's next greater number needs to search circularly, which is also 2.

Note: The length of given array won't exceed 10000.
*/
func nextGreaterElements(nums []int) []int {
	var result []int
	for n, i := range nums {
		result = append(result, find(nums, n+1, i))
	}
	return result
}

func find(nums []int, pos, n int) int {
	perimeter := len(nums)
	for i := pos; i < pos+perimeter; i++ {
		x := nums[i%perimeter]
		if x > n {
			return x
		}
	}
	return -1
}

func comp(a, b []int) bool {
	//fmt.Println(a, b)
	if len(a) != len(b) {
		return false
	}
	for n, i := range a {
		if i != b[n] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(comp(nextGreaterElements([]int{1, 2, 1}), []int{2, -1, 2}))
	fmt.Println(comp(nextGreaterElements([]int{100, 1, 11, 1, 120, 111, 123, 1, -1, -100}),
		[]int{120, 11, 120, 120, 123, 123, -1, 100, 100, 100}))
}
