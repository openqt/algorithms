'''
Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.

53..7....
6..195...
.98....6.
8...6...3
4..8.3..1
7...2...6
.6....28.
...419..5
....8..79

A sudoku puzzle...

534678912
672195348
198342567
859761423
426853791
713924856
961537284
287419635
345286179

...and its solution numbers marked in red. 
'''


class Solution:

    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.solve(board, 0, 0)

    def solve(self, board, row, col):
        if row >= 9:
            return True

        nr = row + 1 if col >= 8 else row
        nc = 0 if col >= 8 else col + 1

        if board[row][col] == '.':
            for v in '123456789':
                board[row][col] = v
                if self.check(board, row, col) and self.solve(board, nr, nc):
                    return True
            board[row][col] = '.'
            return False
        else:
            return self.solve(board, nr, nc)

    def check(self, board, row, col):
        sr = row / 3
        sc = col / 3
        for i in range(9):
            if i != col and board[row][i] == board[row][col]:
                return False
            if i != row and board[i][col] == board[row][col]:
                return False
            r = sr * 3 + i / 3
            c = sc * 3 + i % 3
            if not (r == row and c == col) and board[r][c] == board[row][col]:
                return False
        return True

if __name__ == '__main__':
    board = [
        list('53..7....'),
        list('6..195...'),
        list('.98....6.'),
        list('8...6...3'),
        list('4..8.3..1'),
        list('7...2...6'),
        list('.6....28.'),
        list('...419..5'),
        list('....8..79'), ]

    board = [
        list(".....7..9"),
        list(".4..812.."),
        list("...9...1."),
        list("..53...72"),
        list("293....5."),
        list(".....53.."),
        list("8...23..."),
        list("7...5..4."),
        list("531.7...."), ]
    s = Solution()
    s.solveSudoku(board)
    for i in range(9):
        print board[i]
