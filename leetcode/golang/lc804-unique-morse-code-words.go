package main

import (
	"fmt"
)

/*804. Unique Morse Code Words
https://leetcode.com/problems/unique-morse-code-words/description/

<p>International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: <code>&quot;a&quot;</code> maps to <code>&quot;.-&quot;</code>, <code>&quot;b&quot;</code> maps to <code>&quot;-...&quot;</code>, <code>&quot;c&quot;</code> maps to <code>&quot;-.-.&quot;</code>, and so on.</p>

<p>For convenience, the full table for the 26 letters of the English alphabet is given below:</p>

<pre>
[&quot;.-&quot;,&quot;-...&quot;,&quot;-.-.&quot;,&quot;-..&quot;,&quot;.&quot;,&quot;..-.&quot;,&quot;--.&quot;,&quot;....&quot;,&quot;..&quot;,&quot;.---&quot;,&quot;-.-&quot;,&quot;.-..&quot;,&quot;--&quot;,&quot;-.&quot;,&quot;---&quot;,&quot;.--.&quot;,&quot;--.-&quot;,&quot;.-.&quot;,&quot;...&quot;,&quot;-&quot;,&quot;..-&quot;,&quot;...-&quot;,&quot;.--&quot;,&quot;-..-&quot;,&quot;-.--&quot;,&quot;--..&quot;]</pre>

<p>Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, &quot;cab&quot; can be written as &quot;-.-.-....-&quot;, (which is the concatenation &quot;-.-.&quot; + &quot;-...&quot; + &quot;.-&quot;). We&#39;ll call such a concatenation, the transformation&nbsp;of a word.</p>

<p>Return the number of different transformations among all words we have.</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> words = ["gin", "zen", "gig", "msg"]
<strong>Output:</strong> 2
<strong>Explanation: </strong>
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The length of <code>words</code> will be at most <code>100</code>.</li>
	<li>Each <code>words[i]</code> will have length in range <code>[1, 12]</code>.</li>
    <li><code>words[i]</code> will only consist of lowercase letters.</li>
</ul>
Similar Questions:

*/
func uniqueMorseRepresentations(words []string) int {
    
}

func main() {
	fmt.Println()
}
