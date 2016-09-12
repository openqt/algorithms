'''
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings. 
'''


class Solution:

    # @return a string
    def longestCommonPrefix(self, strs):
        # if not strs or not strs[0]:
        #     return ""
        #
        # first = strs[0]
        # for i in range(len(first)):
        #     for s in strs[1:]:
        #         if i >= len(s) or s[i] != first[i]:
        #             return first[:i]
        # return first

        if strs is None or len(strs) == 0: return ''

        l = min([len(s) for s in strs])
        for i in range(l):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return strs[0][:i]
        return strs[0][:l]


if __name__ == '__main__':
    s = Solution()
    assert s.longestCommonPrefix([]) == ""
    assert s.longestCommonPrefix([""]) == ""
    assert s.longestCommonPrefix(["a", "b"]) == ""
    assert s.longestCommonPrefix(["aa", "aa"]) == "aa"
    print 'PASS'
