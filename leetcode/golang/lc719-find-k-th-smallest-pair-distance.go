package main

import (
	"fmt"
)

/*719. Find K-th Smallest Pair Distance
https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/

Given an integer array, return the k-th smallest **distance** among all the
pairs. The distance of a pair (A, B) is defined as the absolute difference
between A and B.

**Example 1:**  

    
    
    **Input:**
    nums = [1,3,1]
    k = 1
    **Output: 0** 
    **Explanation:**
    Here are all the pairs:
    (1,3) -> 2
    (1,1) -> 0
    (3,1) -> 2
    Then the 1st smallest distance pair is (1,1), and its distance is 0.
    

**Note:**  

  1. `2 <= len(nums) <= 10000`.
  2. `0 <= nums[i] < 1000000`.
  3. `1 <= k <= len(nums) * (len(nums) - 1) / 2`.


Similar Questions:
  Find K Pairs with Smallest Sums (find-k-pairs-with-smallest-sums)
  Kth Smallest Element in a Sorted Matrix (kth-smallest-element-in-a-sorted-matrix)
  Find K Closest Elements (find-k-closest-elements)
  Kth Smallest Number in Multiplication Table (kth-smallest-number-in-multiplication-table)
  K-th Smallest Prime Fraction (k-th-smallest-prime-fraction)
*/
func smallestDistancePair(nums []int, k int) int {
    
}

func main() {
	fmt.Println()
}
