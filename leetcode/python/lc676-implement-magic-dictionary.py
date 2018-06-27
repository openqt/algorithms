# coding=utf-8
import unittest

"""676. Implement Magic Dictionary
https://leetcode.com/problems/implement-magic-dictionary/description/

<p>
Implement a magic directory with <code>buildDict</code>, and <code>search</code> methods.
</p>

<p>
For the method <code>buildDict</code>, you'll be given a list of non-repetitive words to build a dictionary.
</p>

<p>
For the method <code>search</code>, you'll be given a word, and judge whether if you modify <b>exactly</b> one character into <b>another</b> character in this word, the modified word is in the dictionary you just built.
</p>

<p><b>Example 1:</b><br />
<pre>
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>You may assume that all the inputs are consist of lowercase letters <code>a-z</code>.</li>
<li>For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.</li>
<li>Please remember to <b>RESET</b> your class variables declared in class MagicDictionary, as static/class variables are <b>persisted across multiple test cases</b>. Please see <a href="https://leetcode.com/faq/#different-output">here</a> for more details.</li>
</ol>
</p>
Similar Questions:
  Implement Trie (Prefix Tree) (implement-trie-prefix-tree)
  Longest Word in Dictionary (longest-word-in-dictionary)
"""


class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
