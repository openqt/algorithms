package main

import (
	"fmt"
)

/*432. All O`one Data Structure
https://leetcode.com/problems/all-oone-data-structure/description/

Implement a data structure supporting the following operations:

  1. Inc(Key) - Inserts a new key  with value 1. Or increments an existing key by 1. Key is guaranteed to be a **non-empty** string.
  2. Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a **non-empty** string.
  3. GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string `""`.
  4. GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string `""`.

Challenge: Perform all these in O(1) time complexity.


Similar Questions:

*/
type AllOne struct {
    
}


/** Initialize your data structure here. */
func Constructor() AllOne {
    
}


/** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
func (this *AllOne) Inc(key string)  {
    
}


/** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
func (this *AllOne) Dec(key string)  {
    
}


/** Returns one of the keys with maximal value. */
func (this *AllOne) GetMaxKey() string {
    
}


/** Returns one of the keys with Minimal value. */
func (this *AllOne) GetMinKey() string {
    
}


/**
 * Your AllOne object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Inc(key);
 * obj.Dec(key);
 * param_3 := obj.GetMaxKey();
 * param_4 := obj.GetMinKey();
 */

func main() {
	fmt.Println()
}
