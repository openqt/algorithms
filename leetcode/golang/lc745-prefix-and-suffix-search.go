package main

import (
	"fmt"
)

/*745. Prefix and Suffix Search
https://leetcode.com/problems/prefix-and-suffix-search/description/

<p>
Given many <code>words</code>, <code>words[i]</code> has weight <code>i</code>.
</p><p>
Design a class <code>WordFilter</code> that supports one function, <code>WordFilter.f(String prefix, String suffix)</code>.
It will return the word with given <code>prefix</code> and <code>suffix</code> with maximum weight.  If no word exists, return -1.
</p>

<p><b>Examples:</b><br />
<pre>
<b>Input:</b>
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1
</pre></p>

<p><b>Note:</b><br>
<ol>
<li><code>words</code> has length in range <code>[1, 15000]</code>.</li>
<li>For each test case, up to <code>words.length</code> queries <code>WordFilter.f</code> may be made.</li>
<li><code>words[i]</code> has length in range <code>[1, 10]</code>.</li>
<li><code>prefix, suffix</code> have lengths in range <code>[0, 10]</code>.</li>
<li><code>words[i]</code> and <code>prefix, suffix</code> queries consist of lowercase letters only.</li>
</ol>
</p>
Similar Questions:
  Add and Search Word - Data structure design (add-and-search-word-data-structure-design)
*/
type WordFilter struct {
    
}


func Constructor(words []string) WordFilter {
    
}


func (this *WordFilter) F(prefix string, suffix string) int {
    
}


/**
 * Your WordFilter object will be instantiated and called as such:
 * obj := Constructor(words);
 * param_1 := obj.F(prefix,suffix);
 */

func main() {
	fmt.Println()
}
