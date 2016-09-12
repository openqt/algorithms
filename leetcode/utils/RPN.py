# coding=utf-8


class RPN(object):
    """
    Definition for reverse polish notation
    """
    PRIORITY = {
        '+': 10,
        '-': 10,
        '*': 20,
        '/': 20,
        '(': 0,
    }

    def __init__(self, *args):
        self.expr = ''.join(str(i) for i in args)

    def __call__(self, *args, **kwargs):
        if args:
            self.expr = ''.join(str(i) for i in args)
        return self.evalRNP(self.toRPN(self.expr))

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
    assert RPN()('2 + 3 * 4 - (7 - 2) * 3') == -1
