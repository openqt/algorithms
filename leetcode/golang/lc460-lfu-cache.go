package main

import (
	"fmt"
)

/*460. LFU Cache
https://leetcode.com/problems/lfu-cache/description/

<p>Design and implement a data structure for <a href="https://en.wikipedia.org/wiki/Least_frequently_used" target="_blank">Least Frequently Used (LFU)</a> cache. It should support the following operations: <code>get</code> and <code>put</code>.
</p>

<p>
<code>get(key)</code> - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.<br>
<code>put(key, value)</code> - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least <b>recently</b> used key would be evicted.
</p>

<p><b>Follow up:</b><br />
Could you do both operations in <b>O(1)</b> time complexity?</p>

<p><b>Example:</b>
<pre>
LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
</pre>
</p>
Similar Questions:
  LRU Cache (lru-cache)
  Design In-Memory File System (design-in-memory-file-system)
*/
type LFUCache struct {
    
}


func Constructor(capacity int) LFUCache {
    
}


func (this *LFUCache) Get(key int) int {
    
}


func (this *LFUCache) Put(key int, value int)  {
    
}


/**
 * Your LFUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */

func main() {
	fmt.Println()
}
