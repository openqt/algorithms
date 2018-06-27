package main

import (
	"fmt"
)

/*432. All O`one Data Structure
https://leetcode.com/problems/all-oone-data-structure/description/

<p>Implement a data structure supporting the following operations:</p>

<p>
<ol>
<li>Inc(Key) - Inserts a new key <Key> with value 1. Or increments an existing key by 1. Key is guaranteed to be a <b>non-empty</b> string.</li>
<li>Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a <b>non-empty</b> string.</li>
<li>GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string <code>""</code>.</li>
<li>GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string <code>""</code>.</li>
</ol>
</p>

<p>
Challenge: Perform all these in O(1) time complexity.
</p>
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
