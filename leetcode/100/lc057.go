package main

import (
	"fmt"
)

/* 57. Insert Interval
https://leetcode.com/problems/insert-interval/description/

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
	Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
	Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
	This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
*/
/**
 * Definition for an interval.
 * type Interval struct {
 *	   Start int
 *	   End   int
 * }
 */
func insert(intervals []Interval, newInterval Interval) []Interval {
	var result []Interval

	intervals2 := make([]Interval, len(intervals)+1)
	i, j := 0, -1
	for ; i < len(intervals); i++ {
		if j < i && newInterval.Start <= intervals[i].Start {
			j++
			intervals2[j] = newInterval
		}
		j++
		intervals2[j] = intervals[i]
	}
	if j < i {
		intervals2[len(intervals)] = newInterval
	}
	//fmt.Println(intervals2)

	for _, i := range intervals2 {
		if len(result) == 0 {
			result = append(result, i)
		} else {
			last := &result[len(result)-1]
			if !merge(last, i) {
				result = append(result, i)
			}
		}
	}

	//fmt.Println(result)
	return result
}

func merge(a *Interval, b Interval) bool {
	if b.Start <= a.End {
		a.Start, a.End = min(a.Start, b.Start), max(a.End, b.End)
		return true
	}
	return false
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

type Interval struct {
	Start int
	End   int
}

func comp(a, b []Interval) bool {
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
	fmt.Println(comp(insert([]Interval{{1, 5}}, Interval{0, 0}),
		[]Interval{{0, 0}, {1, 5}}))
	fmt.Println(comp(insert([]Interval{{1, 5}}, Interval{2, 3}),
		[]Interval{{1, 5}}))
	fmt.Println(comp(insert([]Interval{}, Interval{5, 7}),
		[]Interval{{5, 7}}))
	fmt.Println(comp(insert([]Interval{{1, 3}, {6, 9}}, Interval{2, 5}),
		[]Interval{{1, 5}, {6, 9}}))
	fmt.Println(comp(insert([]Interval{{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}},
		Interval{4, 9}), []Interval{{1, 2}, {3, 10}, {12, 16}}))
}
