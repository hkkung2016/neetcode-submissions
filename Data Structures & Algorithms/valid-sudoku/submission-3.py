class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True
        boxdict = [defaultdict(bool) for _ in range(9)]
        ## row check
        for i, row in enumerate(board):
            rowdict = defaultdict(bool)
            for j, cell in enumerate(row):
                if cell != ".":
                    if rowdict[cell] == False:
                        rowdict[cell] = True
                    else:
                        return False
                    if boxdict[(j//3)+((i//3)*3)][cell] == False:
                        boxdict[(j//3)+((i//3)*3)][cell] = True
                    else:
                        return False
        ## column check
        row = 0
        while row < 9:
            columndict = defaultdict(bool)
            for i in range(len(board)):
                if board[i][row] != ".":
                    if columndict[board[i][row]] == False:
                        columndict[board[i][row]] = True
                    else:
                        return False
            row += 1
        ## box check
        return True 