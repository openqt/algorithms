package main

import (
	"fmt"
)

/* 496. Next Greater Element I
https://leetcode.com/problems/next-greater-element-i/description/

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
If it does not exist, output -1 for this number.

Example 1:
	Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
	Output: [-1,3,-1]
	Explanation:
		For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
		For number 1 in the first array, the next greater number for it in the second array is 3.
		For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:
	Input: nums1 = [2,4], nums2 = [1,2,3,4].
	Output: [3,-1]
	Explanation:
		For number 2 in the first array, the next greater number for it in the second array is 3.
		For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

Note:
	All elements in nums1 and nums2 are unique.
	The length of both nums1 and nums2 would not exceed 1000.
*/
func nextGreaterElement(findNums []int, nums []int) []int {
	rev := make(map[int]int)
	for n, i := range nums {
		rev[i] = n
	}

	var result []int
	for _, i := range findNums {
		result = append(result, find(nums[rev[i]:], i))
	}
	return result
}

func find(nums []int, n int) int {
	for _, i := range nums {
		if i > n {
			return i
		}
	}
	return -1
}

func comp(a, b []int) bool {
	fmt.Println(a, b)
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
	fmt.Println(comp(nextGreaterElement([]int{4, 1, 2}, []int{1, 3, 4, 2}), []int{-1, 3, -1}))
	fmt.Println(comp(nextGreaterElement([]int{2, 4}, []int{1, 2, 3, 4}), []int{3, -1}))
}
