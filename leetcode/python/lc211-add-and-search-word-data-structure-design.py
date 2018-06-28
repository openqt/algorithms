# coding=utf-8
import unittest

"""211. Add and Search Word - Data structure design
https://leetcode.com/problems/add-and-search-word-data-structure-design/description/

Design a data structure that supports the following two operations:

    
    
    void addWord(word)
    bool search(word)
    

search(word) can search a literal word or a regular expression string
containing only letters `a-z` or `.`. A `.` means it can represent any one
letter.

**Example:**

    
    
    addWord("bad")
    addWord("dad")
    addWord("mad")
    search("pad") -> false
    search("bad") -> true
    search(".ad") -> true
    search("b..") -> true
    

**Note:**  
You may assume that all words are consist of lowercase letters `a-z`.


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
