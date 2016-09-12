'''
Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:

"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5

Note: Do not use the eval built-in library function.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''


class Solution:
    PRIORITY = {
        '+': 10,
        '-': 10,
        '*': 20,
        '/': 20,
        '(': 0,
    }

    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        return self.evalRNP(self.toRPN(s))

    def toRPN(self, s):
        rpn = []
        stack = []

        pos = 0
        while pos < len(s):
            val, pos = self._next(s, pos)
            if isinstance(val, int):
                rpn.append(val)
            elif val == '(':
                stack.append(val)
            elif val == ')':
                while True:
                    n = stack.pop()
                    if n == '(':
                        break
                    rpn.append(n)
            elif val in self.PRIORITY:
                pri = self.PRIORITY[val]
                while len(stack) > 0:
                    n = stack[-1]
                    if self.PRIORITY[n] < pri:
                        break
                    rpn.append(stack.pop())
                stack.append(val)
            # else:
            #     print '>>>', val, pos
        rpn.extend(stack[::-1])
        return rpn

    def _next(self, s, pos):
        t = ''
        while pos < len(s) and '0' <= s[pos] <= '9':
            t += s[pos]
            pos += 1
        if len(t) > 0:
            return int(t), pos
        else:
            pos += 1
            return s[pos-1], pos

    def evalRNP(self, rpn):
        stack = []
        for i in rpn:
            if isinstance(i, int):
                stack.append(i)
            else:
                b, a = stack.pop(), stack.pop()
                if i == '+':
                    stack.append(a + b)
                elif i == '-':
                    stack.append(a - b)
                elif i == '*':
                    stack.append(a * b)
                elif i == '/':
                    stack.append(a / b)
                else:
                    pass
        return stack[0]


if __name__ == '__main__':
    s = Solution()
    print s.calculate('2147483647') == 2147483647
    print s.calculate('3+2*2') == 7
    print s.calculate('3/2') == 1
    print s.calculate('3+5 / 2') == 5
    print 'PASS'
