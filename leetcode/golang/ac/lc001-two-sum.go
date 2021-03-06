package main

import "fmt"

/*1. Two Sum
https://leetcode.com/problems/two-sum/description/

Given an array of integers, return **indices** of the two numbers such that
they add up to a specific target.

You may assume that each input would have **_exactly_** one solution, and you
may not use the _same_ element twice.

**Example:**

    
    
    Given nums = [2, 7, 11, 15], target = 9,
    
    Because nums[ **0** ] + nums[ **1** ] = 2 + 7 = 9,
    return [ **0** , **1** ].


Similar Questions:
  3Sum (3sum)
  4Sum (4sum)
  Two Sum II - Input array is sorted (two-sum-ii-input-array-is-sorted)
  Two Sum III - Data structure design (two-sum-iii-data-structure-design)
  Subarray Sum Equals K (subarray-sum-equals-k)
  Two Sum IV - Input is a BST (two-sum-iv-input-is-a-bst)
*/

/* https://leetcode.com/articles/two-sum/

Approach 3: One-pass Hash Table

It turns out we can do it in one-pass. While we iterate and inserting elements into the table,
we also look back to check if current element's complement already exists in the table.
If it exists, we have found a solution and return immediately.

 */
func twoSum(nums []int, target int) []int {
	cache := make(map[int]int)
	for n, i := range nums {
		val := target - i
		if pos, ok := cache[val]; ok {
			return []int{pos, n}
		}
		cache[i] = n
	}
	return nil
}

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
}
