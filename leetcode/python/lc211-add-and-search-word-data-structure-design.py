# coding=utf-8
import unittest

"""211. Add and Search Word - Data structure design
https://leetcode.com/problems/add-and-search-word-data-structure-design/description/

<p>Design a data structure that supports the following two operations:</p>

<pre>
void addWord(word)
bool search(word)
</pre>

<p>search(word) can search a literal word or a regular expression string containing only letters <code>a-z</code> or <code>.</code>. A <code>.</code> means it can represent any one letter.</p>

<p><strong>Example:</strong></p>

<pre>
addWord(&quot;bad&quot;)
addWord(&quot;dad&quot;)
addWord(&quot;mad&quot;)
search(&quot;pad&quot;) -&gt; false
search(&quot;bad&quot;) -&gt; true
search(&quot;.ad&quot;) -&gt; true
search(&quot;b..&quot;) -&gt; true
</pre>

<p><b>Note:</b><br />
You may assume that all words are consist of lowercase letters <code>a-z</code>.</p>

Similar Questions:
  Implement Trie (Prefix Tree) (implement-trie-prefix-tree)
  Prefix and Suffix Search (prefix-and-suffix-search)
"""


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
