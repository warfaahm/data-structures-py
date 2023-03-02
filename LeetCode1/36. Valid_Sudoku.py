# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated
# according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            x = set()
            for j in range(9):
                current = board[i][j]
                if current == '.':
                    continue
                if current in x:
                    return False
                x.add(current)

        for j in range(9):
            x = set()
            for i in range(9):
                current = board[i][j]
                if current == '.':
                    continue
                if current in x:
                    return False
                x.add(current)
        for i in range(3):
            for j in range(3):
                x = set()
                for y in range(i * 3, i * 3 + 3):
                    for z in range(j * 3, j * 3 + 3):
                        current = board[y][z]
                        if current == '.':
                            continue
                        if current in x:
                            return False
                        x.add(current)
        return True
