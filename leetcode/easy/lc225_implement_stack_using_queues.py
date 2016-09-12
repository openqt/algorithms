'''
Implement Stack using Queues

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
Update (2015-06-11):
The class name of the Java function had been updated to MyStack instead of Stack.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and all test cases.
'''


class Queue:
    def __init__(self):
        self.data = []
    def push(self, x):
        self.data.append(x)
    def top(self):
        return self.data[0]
    def pop(self):
        return self.data.pop(0)
    def empty(self):
        return len(self.data) == 0
    def size(self):
        return len(self.data)
    def __str__(self):
        return ','.join(self.data)

class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.q = Queue()
        self.t = None

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if self.t is not None:
            self.q.push(self.t)
        self.t = x

    # @return nothing
    def pop(self):
        if not self.empty():
            if self.q.size() == 0:
                self.t = None
            else:
                q = self.q
                self.q = Queue()
                while q.size() > 1:
                    self.q.push(q.pop())
                self.t = q.pop()

    # @return an integer
    def top(self):
        return self.t

    # @return an boolean
    def empty(self):
        return self.t is None


if __name__ == '__main__':
    s = Stack()
    for i in 'abcd':
        s.push(i)
    while not s.empty():
        print s.top()
        s.pop()
    print 'PASS'
