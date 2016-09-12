'''
Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB

Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases.
'''


class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        title = ''
        while n > 0:
            n -= 1
            title += chr(n % 26 + ord('A'))
            n /= 26
        return title[::-1]


if __name__ == '__main__':
    s = Solution()
    print s.convertToTitle(1) == 'A'
    print s.convertToTitle(26) == 'Z'
    print s.convertToTitle(703) == 'AAA'
    print s.convertToTitle(52) == 'AZ'
    print s.convertToTitle(3) == 'C'
    print s.convertToTitle(28) == 'AB'
    print 'PASS'
