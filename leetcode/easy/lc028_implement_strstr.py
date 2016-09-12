'''
Implement strStr()

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Update (2014-11-02):
The signature of the function had been updated to return the index instead of the pointer.
If you still see your function signature returns a char * or String, please click the reload button  to reset your code definition.
'''


class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        # return self._bruteforce(haystack, needle)
        # return self._KMP(haystack, needle)
        return self._sunday(haystack, needle)

    def _bruteforce(self, s, w):
        i = j = 0
        while i < len(s) and j < len(w):
            if s[i] == w[j]:
                i += 1; j += 1
            else:
                i = i - j + 1; j = 0
        return i - j if j == len(w) else -1

    def _KMP(self, s, w):
        NEXT = self._buildnext(w)
        print NEXT
        i = j = 0
        while i < len(s) and j < len(w):
            if j < 0 or s[i] == w[j]:
                i += 1; j += 1
            else:
                j = NEXT[j]
        return i - j if j == len(w) else -1

    def _buildnext(self, w):
        NEXT = [-1] * len(w)
        i = 0; k = -1
        while i < len(w)-1:
            if k < 0 or w[i] == w[k]:
                i += 1; k += 1
                NEXT[i] = k
            else:
                k = NEXT[k]
        return NEXT


    def _sunday(self, s, w):
        i = j = 0
        while i < len(s) and j < len(w):
            if s[i] == w[j]:
                i += 1; j += 1
            else:
                i += len(w) - j
                if i > len(s): return -1

                j = self._rindex(w, s[i])
                i = i + 1 if j < 0 else i - j
                j = 0
        return i - j if j == len(w) else -1

    def _rindex(self, w, c):
        i = len(w)-1
        while i >= 0:
            if w[i] == c:
                return i
            i -= 1
        return i

if __name__ == '__main__':
    s = Solution()
    print s.strStr('aeklsio;sdlsdskgABCDABDsdf', 'ABCDABD')
    print s.strStr('substring searching algorithm', 'searchi')
    print s.strStr('LESSONS TEARNED IN SOFTWARE TE', 'SOFTWARE')
    print 'PASS'
