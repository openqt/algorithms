'''
Excel Sheet Column Number

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''


class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        num = 0
        for i in s:
            num = num * 26 + ord(i) - ord('A') + 1
        return num


if __name__ == '__main__':
    s = Solution()
    print s.titleToNumber('C') == 3
    print s.titleToNumber('AB') == 28
    print s.titleToNumber('AAA')
    print 'PASS'
