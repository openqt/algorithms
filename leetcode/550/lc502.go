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

// An Item is something we manage in a priority queue.
type Item struct {
	value    int // The value of the item; arbitrary.
	priority int // The priority of the item in the queue.
	index    int // The index of the item in the heap.
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue struct {
	Q     []*Item
	Count int
	Inc   bool // increase
}

func (pq PriorityQueue) Len() int { return pq.Count }

func (pq *PriorityQueue) Push(x *Item) {
	if x.index > 0 {
		pq.Q[x.index] = x
	} else {
		pq.Q = append(pq.Q, x)
		x.index = len(pq.Q) - 1
	}
	pq.Count += 1
}

func (pq *PriorityQueue) Top() *Item {
	if pq.Count <= 0 {
		pq.Q = nil
		return nil
	}

	var val *Item
	for _, i := range pq.Q {
		if i != nil {
			if val == nil {
				val = i
			}

			if pq.Inc {
				if i.priority < val.priority {
					val = i
				}
			} else {
				if i.priority > val.priority {
					val = i
				}
			}
		}
	}
	return val
}

func (pq *PriorityQueue) Pop() *Item {
	val := pq.Top()
	if val != nil {
		pq.Q[val.index] = nil
		pq.Count -= 1
	}
	return val
}

func findMaximizedCapital(k int, W int, Profits []int, Capital []int) int {
	oriq := PriorityQueue{Inc: true}
	valq := PriorityQueue{Inc: false}

	for n, c := range Capital {
		oriq.Push(&Item{value: Profits[n], priority: c})
	}

	for ; k > 0; k-- {
		for oriq.Len() > 0 && oriq.Top().priority <= W {
			val := oriq.Pop()
			valq.Push(&Item{value: val.value, priority: val.value})
		}

		if valq.Len() == 0 {
			break
		}
		W += valq.Pop().value
	}

	return W
}

func main() {
	fmt.Println(findMaximizedCapital(2, 0, []int{1, 2, 3}, []int{0, 1, 1}) == 4)
	fmt.Println(findMaximizedCapital(3, 0, []int{1, 2, 3}, []int{0, 1, 2}) == 6)
	fmt.Println(findMaximizedCapital(1, 0, []int{1, 2, 3}, []int{0, 1, 2}) == 1)
	fmt.Println(findMaximizedCapital(1, 0, []int{1, 2, 3}, []int{1, 1, 2}) == 0)
	fmt.Println(findMaximizedCapital(1, 2, []int{1, 2, 3}, []int{1, 1, 2}) == 5)
}
