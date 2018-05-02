package main

import (
	"fmt"
	"strconv"
)

/*412. Fizz Buzz
https://leetcode.com/problems/fizz-buzz/description/

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for
the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:
	n = 15,
	Return:
	[
		"1",
		"2",
		"Fizz",
		"4",
		"Buzz",
		"Fizz",
		"7",
		"8",
		"Fizz",
		"Buzz",
		"11",
		"Fizz",
		"13",
		"14",
		"FizzBuzz"
	]
*/
func fizzBuzz(n int) []string {
	vals := make([]string, n)
	for i := 3; i <= n; i += 3 {
		vals[i-1] = "Fizz"
	}
	for i := 5; i <= n; i += 5 {
		vals[i-1] += "Buzz"
	}
	for i := 0; i < n; i++ {
		if vals[i] == "" {
			vals[i] = strconv.Itoa(i + 1)
		}
	}
	return vals
}

func main() {
	fmt.Println(fizzBuzz(15))
}
