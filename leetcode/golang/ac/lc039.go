package main

import (
	"fmt"
	"sort"
)

/*39. Combination Sum
https://leetcode.com/problems/combination-sum/description/

Given a set of candidate numbers (C) (without duplicates) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
	All numbers (including target) will be positive integers.
	The solution set must not contain duplicate combinations.

For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
	[
	  [7],
	  [2, 2, 3]
	]
*/
func combinationSum(candidates []int, target int) [][]int {
	var book [][]int
	for n, i := range candidates {
		find(candidates[n:], target-i, []int{i}, &book)
	}

	//for _, i := range book {
	//	fmt.Println(i)
	//}
	return book
}

func find(candidates []int, target int, link []int, book *[][]int) {
	if target == 0 {
		*book = append(*book, link)
	} else if target > 0 {
		for n, i := range candidates {
			data := make([]int, len(link))
			copy(data, link)
			find(candidates[n:], target-i, append(data, i), book)
		}
	}
}

func compare(a, b [][]int) bool {
	if len(a) != len(b) {
		return false
	}
	book := make(map[string]int)
	for n, i := range a {
		sort.Ints(i)
		book[fmt.Sprintf("%v", i)] = n
	}
	for _, i := range b {
		sort.Ints(i)
		key := fmt.Sprintf("%v", i)
		if _, ok := book[key]; !ok {
			return false
		}
		delete(book, key)

	}
	return len(book) == 0
}

func main() {
	fmt.Println(compare(combinationSum([]int{2, 3, 6, 7}, 7), [][]int{{7}, {2, 2, 3}}))
	fmt.Println(compare(combinationSum([]int{1, 2}, 4), [][]int{{1, 1, 1, 1}, {1, 1, 2}, {2, 2}}))
	fmt.Println(compare(
		combinationSum([]int{33, 28, 25, 45, 26, 27, 47, 29, 32, 21, 37, 35, 48, 49, 40, 39, 41, 46, 20, 24, 30, 36, 38, 44, 23, 34}, 51),
		[][]int{{28, 23}, {25, 26}, {27, 24}, {21, 30}}))
}
