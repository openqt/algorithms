package main

/*88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/description/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
	You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold
	additional elements from nums2.
	The number of elements initialized in nums1 and nums2 are m and n respectively.
*/
func merge(nums1 []int, m int, nums2 []int, n int) {
	for p := m + n - 1; p >= 0; p-- {
		if m <= 0 {
			nums1[p] = nums2[n-1]
			n--
		} else if n <= 0 {
			nums1[p] = nums1[m-1]
			m--
		} else {
			if nums1[m-1] < nums2[n-1] {
				nums1[p] = nums2[n-1]
				n--
			} else {
				nums1[p] = nums1[m-1]
				m--
			}
		}
	}
}

func main() {
}
