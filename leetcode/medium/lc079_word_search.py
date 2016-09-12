# coding=utf-8
"""
079. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example,
    Given board =

    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]

word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""


class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.word = word
        self.rows = len(board)
        self.cols = len(board[0])

        for row in range(self.rows):
            for col in range(self.cols):
                if self.dfs(row, col, 0):
                    return True
        return False

    def dfs(self, row, col, pos):
        if pos >= len(self.word):
            return True

        if row < 0 or row >= self.rows or \
           col < 0 or col >= self.cols or \
           self.word[pos] != self.board[row][col]:
            return False

        self.board[row][col] = ''
        ret = self.dfs(row-1, col, pos+1) or \
              self.dfs(row, col+1, pos+1) or \
              self.dfs(row+1, col, pos+1) or \
              self.dfs(row, col-1, pos+1)
        self.board[row][col] = self.word[pos]
        return ret


if __name__ == '__main__':
    s = Solution()

    board = [['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']]
    assert s.exist(board, 'ABCCED')
    assert s.exist(board, 'SEE')
    assert not s.exist(board, 'ABCB')

    board = [list("aaaa"), list("aaaa"), list("aaaa")]
    assert s.exist(board, "aaaaaaaaaaaa")

    board = [list("aaaa"), list("aaaa"), list("aaaa"), list("aaaa"), list("aaaa")]
    assert s.exist(board, "aaaaaaaaaaaaaaaaaaaa")

    print 'PASS'
