package main

import (
    "fmt"
)

/*307. Range Sum Query - Mutable
https://leetcode.com/problems/range-sum-query-mutable/description/

Given an integer array _nums_ , find the sum of the elements between indices
_i_ and _j_ ( _i_ ≤ _j_ ), inclusive.

The _update(i, val)_ function modifies _nums_ by updating the element at index
_i_ to _val_.

**Example:**

    
    
    Given nums = [1, 3, 5]
    
    sumRange(0, 2) -> 9
    update(1, 2)
    sumRange(0, 2) -> 8
    

**Note:**

  1. The array is only modifiable by the _update_ function.
  2. You may assume the number of calls to _update_ and _sumRange_ function is distributed evenly.


Similar Questions:
  Range Sum Query - Immutable (range-sum-query-immutable)
  Range Sum Query 2D - Mutable (range-sum-query-2d-mutable)
*/
type NumArray struct {
    
}


func Constructor(nums []int) NumArray {
    
}


func (this *NumArray) Update(i int, val int)  {
    
}


func (this *NumArray) SumRange(i int, j int) int {
    
}


/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * obj.Update(i,val);
 * param_2 := obj.SumRange(i,j);
 */

func main() {
    fmt.Println()
}
