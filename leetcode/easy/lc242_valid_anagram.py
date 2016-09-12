'''
Valid Anagram

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
'''

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    s = Solution()
    print s.isAnagram('anagram', 'nagaram')
    print not s.isAnagram('rat', 'car')
    print 'PASS'
