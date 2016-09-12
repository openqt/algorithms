'''
Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
'''


class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        last = len(s)
        if last == 0: return 0

        while s[last-1] == ' ' and last > 0:
            last -= 1
        total = last

        while last > 0:
            if s[last-1] == ' ': break
            last -= 1
        return total - last


if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLastWord('Hello World')
    print s.lengthOfLastWord('a')
    print s.lengthOfLastWord('a ')
    print s.lengthOfLastWord('')

    print 'PASS'
