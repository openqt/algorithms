# coding=utf-8
import unittest

"""232. Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/description/

Implement the following operations of a queue using stacks.

  * push(x) -- Push element x to the back of queue.
  * pop() -- Removes the element from in front of queue.
  * peek() -- Get the front element.
  * empty() -- Return whether the queue is empty.

**Example:**

    
    
    MyQueue queue = new MyQueue();
    
    queue.push(1);
    queue.push(2);  
    queue.peek();  // returns 1
    queue.pop();   // returns 1
    queue.empty(); // returns false

**Notes:**

  * You must use _only_ standard operations of a stack -- which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid.
  * Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
  * You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).


Similar Questions:
  Implement Stack using Queues (implement-stack-using-queues)
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
