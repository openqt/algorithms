package main

import (
    "fmt"
)

/*986. Interval List Intersections
https://leetcode.com/problems/interval-list-intersections/description/

Given two lists of **closed** intervals, each list of intervals is pairwise
disjoint and in sorted order.

Return the intersection of these two interval lists.

_(Formally, a closed interval`[a, b]` (with `a <= b`) denotes the set of real
numbers `x` with `a <= x <= b`.  The intersection of two closed intervals is a
set of real numbers that is either empty, or can be represented as a closed
interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)_



**Example 1:**

**![](https://assets.leetcode.com/uploads/2019/01/30/interval1.png)**

    
    
    **Input:** A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
    **Output:** [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    **Reminder:** The inputs and the desired output are lists of Interval objects, and not arrays or lists.
    



**Note:**

  1. `0 <= A.length < 1000`
  2. `0 <= B.length < 1000`
  3. `0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9`


Similar Questions:

*/
/**
 * Definition for an interval.
 * type Interval struct {
 *	   Start int
 *	   End   int
 * }
 */
func intervalIntersection(A []Interval, B []Interval) []Interval {
    
}

func main() {
    fmt.Println()
}
