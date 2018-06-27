package main

import "fmt"

/*349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/description/

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
	Each element in the result must be unique.
	The result can be in any order.
*/
func intersection(nums1 []int, nums2 []int) []int {
	book := make(map[int]int)
	for _, i := range nums1 {
		book[i]++
	}
	var result []int
	for _, i := range nums2 {
		if book[i] > 0 {
			book[i] = 0
			result = append(result, i)
		}
	}
	return result
}

func main() {
	fmt.Println()
}
