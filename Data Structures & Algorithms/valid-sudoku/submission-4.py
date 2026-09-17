class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxdict = [0] * 9
        rowdict = [0] * 9
        coldict = [0] * 9
        ## row check
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == ".":
                    continue
                bit = 1 << int(board[i][j])
                if rowdict[i] & bit != 0 or coldict[j] & bit != 0 or boxdict[(j//3)+((i//3)*3)] & bit != 0:
                    return False
                else:
                    rowdict[i] |= bit
                    coldict[j] |= bit
                    boxdict[(j//3)+((i//3)*3)] |= bit
        return True 