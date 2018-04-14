package main

import "fmt"

/*118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/description/

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
*/
func generate(numRows int) [][]int {
	if numRows <= 0 {
		return [][]int{}
	}
	tri := [][]int{{1}}
	for numRows -= 1; numRows > 0; numRows-- {
		last := tri[len(tri)-1]
		array := make([]int, len(last)+1)
		for i := 1; i < len(array)-1; i++ {
			array[i] = last[i-1] + last[i]
		}
		array[0], array[len(array)-1] = 1, 1
		tri = append(tri, array)
	}
	return tri
}

func main() {
	fmt.Println(generate(6))
}
