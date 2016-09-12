'''
Valid Sudoku

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty nums are filled with the character '.'.

53..7....
6..195...
.98....6.
8...6...3
4..8.3..1
7.3323336
.6....28.
...419..5
....8..79

A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled nums need to be validated.
'''


class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        self.board = board
        for i in range(9):
            if not self.isValidByRow(i): return False
            if not self.isValidByCol(i): return False
            if not self.isValidByCell(i): return False
        return True

    def isValidByRow(self, row):
        nums = {str(i): True for i in range(1, 10)}
        for i in range(9):
            if not self._check(nums, row, i):
                return False
        return True

    def isValidByCol(self, col):
        nums = {str(i): True for i in range(1, 10)}
        for i in range(9):
            if not self._check(nums, i, col):
                return False
        return True

    def isValidByCell(self, cell):
        nums = {str(i): True for i in range(1, 10)}
        pins = [(0, 0), (0, 3), (0, 6),
               (3, 0), (3, 3), (3, 6),
               (6, 0), (6, 3), (6, 6), ]
        pos = pins[cell]
        for i in range(3):
            for j in range(3):
                if not self._check(nums, i+pos[0], j+pos[1]):
                    return False
        return True

    def _check(self, nums, row, col):
        pin = self.board[row][col]
        if pin == '.':
            return True
        if nums[pin]:
            nums[pin] = False
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    assert not s.isValidSudoku(["..4...63.", ".........", "5......9.", "...56....",
                                "4.3.....1", "...7.....", "...5.....", ".........", "........."])
    assert not s.isValidSudoku([".........", ".........", ".9......1", "8........",
                                ".99357...", ".......4.", "...8.....", ".1....4.9", "...5.4..."])
    print 'PASS'
