# coding=utf-8
import unittest

"""284. Peeking Iterator
https://leetcode.com/problems/peeking-iterator/description/

<p>Given an Iterator class interface with methods: <code>next()</code> and <code>hasNext()</code>, design and implement a PeekingIterator that support the <code>peek()</code> operation -- it essentially peek() at the element that will be returned by the next call to next().</p>

<p><strong>Example:</strong></p>

<pre>
Assume that the iterator is initialized to the beginning of the list: <strong><code>[1,2,3]</code></strong>.

Call <strong><code>next()</code></strong> gets you <strong>1</strong>, the first element in the list.
Now you call <strong><code>peek()</code></strong> and it returns <strong>2</strong>, the next element. Calling <strong><code>next()</code></strong> after that <i><b>still</b></i> return <strong>2</strong>. 
You call <strong><code>next()</code></strong> the final time and it returns <strong>3</strong>, the last element. 
Calling <strong><code>hasNext()</code></strong> after that should return <strong>false</strong>.
</pre>

<p><b>Follow up</b>: How would you extend your design to be generic and work with all types, not just integer?</p>

Similar Questions:
  Binary Search Tree Iterator (binary-search-tree-iterator)
  Flatten 2D Vector (flatten-2d-vector)
  Zigzag Iterator (zigzag-iterator)
"""


# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        

    def next(self):
        """
        :rtype: int
        """
        

    def hasNext(self):
        """
        :rtype: bool
        """
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
