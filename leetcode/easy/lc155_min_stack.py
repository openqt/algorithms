'''
Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''


class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.min = None
        self.stack = []
        self.minstack = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if self.min is None or x <= self.min:
            self.minstack.append(x)
            self.min = x

    # @return nothing
    def pop(self):
        if self.stack:
            t = self.stack.pop(-1)
            if t <= self.min:
                self.minstack.pop(-1)
                self.min = self.minstack[-1] if self.minstack else None

    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.min


if __name__ == '__main__':
    s = MinStack()
    s.push(2)
    s.push(0)
    s.push(3)
    s.push(0)
    print s.getMin()
    s.pop()
    print s.getMin()
    s.pop()
    print s.getMin()
    s.pop()
    print s.getMin()
    print 'PASS'
