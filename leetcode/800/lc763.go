package main

import (
	"fmt"
)

/*763. Partition Labels
https://leetcode.com/problems/partition-labels/description/

A string S of lowercase letters is given.
We want to partition this string into as many parts as possible so that each letter appears in at most one part,
and return a list of integers representing the size of these parts.

Example 1:
	Input: S = "ababcbacadefegdehijhklij"
	Output: [9,7,8]
	Explanation:
	The partition is "ababcbaca", "defegde", "hijhklij".
	This is a partition so that each letter appears in at most one part.
	A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:
	S will have length in range [1, 500].
	S will consist of lowercase letters ('a' to 'z') only.
*/
func partitionLabels(S string) []int {
	book := make(map[rune][]int)
	for n, i := range S {
		book[i] = append(book[i], n)
	}

	wall := make([]bool, len(S))
	for _, v := range book {
		//fmt.Printf("%c: %v\n", k, v)
		if len(v) > 1 {
			for i := v[0]; i < v[len(v)-1]; i++ {
				wall[i] = true
			}
		}
	}
	//fmt.Println(wall)

	var result []int
	count := 1
	for _, i := range wall {
		if i {
			count++
		} else {
			result = append(result, count)
			count = 1
		}
	}
	return result
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
	fmt.Println(comp(partitionLabels("ababcbacadefegdehijhklij"), []int{9, 7, 8}))
}
