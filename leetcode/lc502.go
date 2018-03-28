package main

import (
	"fmt"
)

/* 502. IPO
https://leetcode.com/problems/ipo/description/

Suppose LeetCode will start its IPO soon.
In order to sell a good price of its shares to Venture Capital,
LeetCode would like to work on some projects to increase its capital before the IPO.
Since it has limited resources, it can only finish at most k distinct projects before the IPO.
Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given several projects.
For each project i, it has a pure profit Pi and a minimum capital of Ci is needed to start the corresponding project.
Initially, you have W capital.
When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

To sum up, pick a list of at most k distinct projects from given projects to maximize your final capital,
and output your final maximized capital.

Example 1:
	Input: k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].

	Output: 4

	Explanation: Since your initial capital is 0, you can only start the project indexed 0.
				 After finishing it you will obtain profit 1 and your capital becomes 1.
				 With capital 1, you can either start the project indexed 1 or the project indexed 2.
				 Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
				 Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
Note:
	You may assume all numbers in the input are non-negative integers.
	The length of Profits array and Capital array will not exceed 50,000.
	The answer is guaranteed to fit in a 32-bit signed integer.
*/
func max(a, b complex128) complex128 {
	if real(a) > real(b) {
		return a
	}
	return b
}

type Cell struct {
	Max, Cap int
}

func findMaximizedCapital(k int, W int, Profits []int, Capital []int) int {
	memo := make([][]Cell, len(Profits))
	for i := 0; i < len(memo); i++ {
		memo[i] = make([]Cell, k+1)
	}
	for row := 0; row < len(memo); row++ {
		memo[row][0] = Cell{0, W}
	}
	for col := 1; col <= k; col++ {
		if W >= Capital[0] {
			memo[0][col] = Cell{Profits[0], Profits[0]+W-Capital[0]}
		} else {
			memo[0][col] = Cell{0, W}
		}
	}

	for col := 1; col <= k; col++ {
		for row := 1; row < len(memo); row++ {
			up := memo[row-1][col]
			if row < col {
				if up.Cap >= Capital[row] {
					memo[row][col] = Cell{up.Max + Profits[row], up.Cap - Capital[row] + Profits[row]}
				} else {
					memo[row][col] = up
				}
			} else {


			}
		}
	}

	for i := 0; i < len(memo); i++ {
		fmt.Println(memo[i])
	}
	fmt.Println(memo[len(memo)-1][k])

	return memo[len(memo)-1][k].Max
}

// 参考：http://blog.csdn.net/makuiyu/article/details/43698963
func main() {
	fmt.Println(findMaximizedCapital(2, 0, []int{1, 2, 3}, []int{0, 1, 1}) == 4)
	//fmt.Println(findMaximizedCapital(3, 0, []int{1, 2, 3}, []int{0, 1, 2}) == 6)
}
