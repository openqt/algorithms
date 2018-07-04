package main

import (
	"fmt"
	"sort"
)

/*216. Combination Sum III
https://leetcode.com/problems/combination-sum-iii/description/

Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

	Input: k = 3, n = 7

	Output:

	[[1,2,4]]

Example 2:

	Input: k = 3, n = 9

	Output:

	[[1,2,6], [1,3,5], [2,3,4]]
*/
func combinationSum3(k int, n int) [][]int {
	var book [][]int
	for i := 1; i <= 9; i++ {
		find(i, k-1, n-i, []int{i}, &book)
	}

	//fmt.Println(book)
	return book
}

func find(s, k, n int, link []int, book *[][]int) {
	if k == 0 {
		if n == 0 {
			data := make([]int, len(link))
			copy(data, link)
			*book = append(*book, data)
		}
		return
	}

	if n > 0 {
		for i := s + 1; i <= 9; i++ {
			find(i, k-1, n-i, append(link, i), book)
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

func compare(a, b [][]int) bool {
	if len(a) != len(b) {
		return false
	}
	book := make(map[string]int)
	for n, i := range a {
		book[key(i)] = n
	}
	for _, i := range b {
		k := key(i)
		if _, ok := book[k]; !ok {
			return false
		}
		delete(book, k)

	}
	return len(book) == 0
}

func main() {
	fmt.Println(compare(combinationSum3(3, 7), [][]int{{1, 2, 4}}))
	fmt.Println(compare(combinationSum3(3, 9), [][]int{{1, 3, 5}, {2, 3, 4}, {1, 2, 6}}))
}
