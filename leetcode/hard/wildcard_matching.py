#-*-encoding:utf-8-*-
'''
Wildcard Matching

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''


class Solution:

    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        # s pointer, p pointer, star: s and p position
        sp, pp, ss, ps = 0, 0, -1, -1
        while sp < len(s):
            if pp < len(p) and p[pp] in ('?', s[sp]):
                sp += 1
                pp += 1  # match, go ahead
            elif pp < len(p) and p[pp] == '*':
                pp += 1
                ss = sp
                # for *, p pointer go next, ss, ps save current sp and pp
                ps = pp
            elif ps > -1:
                pp = ps
                ss += 1
                sp = ss  # not match, back to last star position, ss increase
            else:
                return False  # not match
        while pp < len(p) and p[pp] == '*':
            pp += 1
        return pp == len(p)

if __name__ == '__main__':
    s = Solution()
    assert not s.isMatch("aa", "a")
    assert s.isMatch("aa", "aa")
    assert not s.isMatch("aaa", "aa")
    assert s.isMatch("aa", "*")
    assert s.isMatch("aa", "a*")
    assert s.isMatch("ab", "?*")
    assert not s.isMatch("aab", "c*a*b")
    assert s.isMatch("a", "a*")
    assert not s.isMatch("a", "aa")
    assert s.isMatch("abcdef", "a*f")
    assert s.isMatch("c", "*?*")
    assert s.isMatch("hi", "*?")
    assert not s.isMatch("", "?")
    assert not s.isMatch("b", "*?*?")
    assert s.isMatch("aaaabaaaab", "a*b*b")
    print "PASS"
