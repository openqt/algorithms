package main

import (
	"fmt"
	"sort"
)

/*40. Combination Sum II
https://leetcode.com/problems/combination-sum-ii/description/

Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
	All numbers (including target) will be positive integers.
	The solution set must not contain duplicate combinations.

For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
	[
	  [1, 7],
	  [1, 2, 5],
	  [2, 6],
	  [1, 1, 6]
	]
*/
func combinationSum2(candidates []int, target int) [][]int {
	book := make(map[string]int)
	for n, i := range candidates {
		find(candidates[n+1:], target-i, []int{i}, book)
	}

	var data [][]int
	for i := range book {
		data = append(data, val(i))
	}
	fmt.Println(data)
	return data
}

func find(candidates []int, target int, link []int, book map[string]int) {
	if target == 0 {
		book[key(link)] += 1
	} else if target > 0 {
		for n, i := range candidates {
			data := make([]int, len(link))
			copy(data, link)
			find(candidates[n+1:], target-i, append(data, i), book)
		}
	}
}

func key(is []int) string {
	key := ""
	sort.Ints(is)
	for _, i := range is {
		key += string(i)
	}
	return key
}

func val(key string) []int {
	var is []int
	for _, i := range key {
		is = append(is, int(i))
	}
	return is
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
	//fmt.Println(compare(combinationSum2([]int{10, 1, 2, 7, 6, 1, 5}, 8), [][]int{{1, 7}, {1, 2, 5}, {2, 6}, {1, 1, 6}}))
	fmt.Println(compare(combinationSum2([]int{3, 1, 3, 5, 1, 1}, 8), [][]int{{1, 1, 1, 5}, {1, 1, 3, 3}, {3, 5}}))
}
