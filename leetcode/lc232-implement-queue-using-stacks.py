# coding=utf-8
import unittest

"""Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/description/

<p>Implement the following operations of a queue using stacks.</p>

<ul>
	<li>push(x) -- Push element x to the back of queue.</li>
	<li>pop() -- Removes the element from in front of queue.</li>
	<li>peek() -- Get the front element.</li>
	<li>empty() -- Return whether the queue is empty.</li>
</ul>

<p><b>Example:</b></p>

<pre>
MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false</pre>

<p><b>Notes:</b></p>

<ul>
	<li>You must use <i>only</i> standard operations of a stack -- which means only <code>push to top</code>, <code>peek/pop from top</code>, <code>size</code>, and <code>is empty</code> operations are valid.</li>
	<li>Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.</li>
	<li>You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).</li>
</ul>

"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
