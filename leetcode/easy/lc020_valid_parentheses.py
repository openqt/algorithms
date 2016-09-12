'''
Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        M = {')': '(', ']': '[', '}': '{'}

        stack = []
        for i in s:
            if i in {'(', '[', '{'}:
                stack.append(i)
            if i in M:
                if not stack or stack.pop() != M[i]:
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    print s.isValid('()')
    print s.isValid('()[]{}')
    print not s.isValid('(]')
    print not s.isValid('([)]')
    print not s.isValid(']')
    print not s.isValid('[')
    print 'PASS'
