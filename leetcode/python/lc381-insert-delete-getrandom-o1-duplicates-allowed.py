# coding=utf-8
import unittest

"""381. Insert Delete GetRandom O(1) - Duplicates allowed
https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/

<p>Design a data structure that supports all following operations in <i>average</i> <b>O(1)</b> time.</p>
<b>Note: Duplicate elements are allowed.</b>
<p>
<ol>
<li><code>insert(val)</code>: Inserts an item val to the collection.</li>
<li><code>remove(val)</code>: Removes an item val from the collection if present.</li>
<li><code>getRandom</code>: Returns a random element from current collection of elements. The probability of each element being returned is <b>linearly related</b> to the number of same value the collection contains.</li>
</ol>
</p>

<p><b>Example:</b>
<pre>
// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
</pre>
</p>
"""


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
