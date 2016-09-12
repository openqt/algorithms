'''
Word Break II

Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"]. 
'''


class Solution:

    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        self.words = []
        self.dfs(s, dict, '')
        return self.words

    def dfs(self, s, dict, words):
        if not self.isBreak(s, dict, set()):
            return

        if not s:
            self.words.append(words[1:])
            return

        for i in range(1, len(s) + 1):
            if s[:i] in dict:
                self.dfs(s[i:], dict, words + ' ' + s[:i])

    def isBreak(self, s, dict, map):
        if not s:
            return True
        for i in range(1, len(s) + 1):
            if s[:i] in dict:
                if s[i:] not in map:
                    if self.isBreak(s[i:], dict, map):
                        return True
                    else:
                        map.add(s[i:])
        return False

if __name__ == '__main__':
    s = Solution()
    print s.wordBreak('catsanddog', {"cat", "cats", "and", "sand", "dog"})
    print s.wordBreak('a', {'a'})
    print s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", {"a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"})
