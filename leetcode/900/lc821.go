package main

import (
	"fmt"
)

/*821. Shortest Distance to a Character
https://leetcode.com/problems/shortest-distance-to-a-character/description/

Given a string S and a character C,
return an array of integers representing the shortest distance from the character C in the string.

Example 1:
	Input: S = "loveleetcode", C = 'e'
	Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

Note:
	S string length is in [1, 10000].
	C is a single character, and guaranteed to be in string S.
	All letters in S and C are lowercase.
*/
func shortestToChar(S string, C byte) []int {
	max := len(S)
	dist := make([]int, max)

	v := max
	for n, i := range S {
		if byte(i) == C {
			v = 0
		} else {
			v++
		}
		dist[n] = v
	}

	v = max
	for i := max - 1; i >= 0; i-- {
		if byte(S[i]) == C {
			v = 0
		} else {
			v++
		}
		if dist[i] > v {
			dist[i] = v
		}
	}

	return dist
}

func main() {
	fmt.Println(shortestToChar("loveleetcode", 'e'))
}
