package main

import (
	"fmt"
)

/*677. Map Sum Pairs
https://leetcode.com/problems/map-sum-pairs/description/

<p>
Implement a MapSum class with <code>insert</code>, and <code>sum</code> methods.
</p>

<p>
For the method <code>insert</code>, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.
</p>

<p>
For the method <code>sum</code>, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.
</p>

<p><b>Example 1:</b><br />
<pre>
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
</pre>
</p>

Similar Questions:

*/
type MapSum struct {
    
}


/** Initialize your data structure here. */
func Constructor() MapSum {
    
}


func (this *MapSum) Insert(key string, val int)  {
    
}


func (this *MapSum) Sum(prefix string) int {
    
}


/**
 * Your MapSum object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(key,val);
 * param_2 := obj.Sum(prefix);
 */

func main() {
	fmt.Println()
}
