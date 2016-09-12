'''
Implement Queue using Stacks

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively.
You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
'''

class Stack:
    def __init__(self):
        self.data = []
    def push(self, x):
        self.data.append(x)
    def top(self):
        return self.data[-1]
    def pop(self):
        return self.data.pop()
    def empty(self):
        return len(self.data) == 0
    def size(self):
        return len(self.data)
    def __str__(self):
        return ','.join(self.data)

class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.data = Stack()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        pre = Stack()
        while not self.empty():
            pre.push(self.peek())
            self.pop()
        pre.push(x)
        while not pre.empty():
            self.data.push(pre.pop())

    # @return nothing
    def pop(self):
        self.data.pop()

    # @return an integer
    def peek(self):
        return self.data.top()

    # @return an boolean
    def empty(self):
        return self.data.empty()


if __name__ == '__main__':
    s = Queue()
    for i in 'abcd':
        s.push(i)
    while not s.empty():
        print s.peek()
        s.pop()
    print 'PASS'
