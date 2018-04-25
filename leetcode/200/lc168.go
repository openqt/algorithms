package main

import (
	"fmt"
)

/*168. Excel Sheet Column Title
https://leetcode.com/problems/excel-sheet-column-title/description/

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...

Example 1:
	Input: 1
	Output: "A"

Example 2:
	Input: 28
	Output: "AB"

Example 3:
	Input: 701
	Output: "ZY"
*/
func convertToTitle(n int) string {
	const BASE = 26
	val := ""
	for i := n; i > 0; i = (i - 1) / BASE {
		val = string((i-1)%BASE+'A') + val
	}
	//fmt.Println(val)
	return val
}

func main() {
	fmt.Println(convertToTitle(1) == "A")
	fmt.Println(convertToTitle(26) == "Z")
	fmt.Println(convertToTitle(27) == "AA")
	fmt.Println(convertToTitle(28) == "AB")
	fmt.Println(convertToTitle(29) == "AC")
	fmt.Println(convertToTitle(54) == "BB")
	fmt.Println(convertToTitle(701) == "ZY")
}
