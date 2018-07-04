package main

import (
	"fmt"
)

/* 56. Merge Intervals
https://leetcode.com/problems/merge-intervals/description/

Given a collection of intervals, merge all overlapping intervals.

For example,
	Given [1,3],[2,6],[8,10],[15,18],
	return [1,6],[8,10],[15,18].
*/
/**
 * Definition for an interval.
 * type Interval struct {
 *	   Start int
 *	   End   int
 * }
 */
func merge(intervals []Interval) []Interval {
	var result []Interval
	sort(intervals)
	for _, i := range intervals {
		if len(result) == 0 {
			result = append(result, i)
		} else {
			last := &result[len(result)-1]
			if i.Start <= last.End {
				last.Start, last.End = min(last.Start, i.Start), max(last.End, i.End)
			} else {
				result = append(result, i)
			}
		}
	}
	return result
}

func sort(a []Interval) {
	for i := 0; i < len(a); i++ {
		for j := i + 1; j < len(a); j++ {
			if a[i].Start > a[j].Start {
				a[i], a[j] = a[j], a[i]
			}
		}
	}
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
	fmt.Println(comp(merge([]Interval{{1, 3}, {2, 6}, {8, 10}, {15, 18}}),
		[]Interval{{1, 6}, {8, 10}, {15, 18}}))
	fmt.Println(comp(merge([]Interval{{1, 4}, {0, 0}}),
		[]Interval{{0, 0}, {1, 4}}))
}
