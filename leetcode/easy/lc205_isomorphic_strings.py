'''
Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
'''

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if len(s) != len(t): return False

        m = {}; mm = set()
        for i in range(len(s)):
            a = s[i]; b = t[i]
            if a in m:
                if m[a] != b: return False
            elif b in mm:
                return False
            else:
                m[a] = b
                mm.add(b)
        return True

if __name__ == '__main__':
    s = Solution()
    assert not s.isIsomorphic('ab', 'aa')
    assert s.isIsomorphic('egg', 'add')
    assert not s.isIsomorphic('foo', 'bar')
    assert s.isIsomorphic('paper', 'title')
    print 'PASS'
