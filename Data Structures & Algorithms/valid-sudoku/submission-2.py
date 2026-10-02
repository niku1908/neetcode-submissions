class Solution:

    def check(self, row, col, board, mapping, mapping_col):

        new_row = row-(row%3)
        new_col = col-(col%3)
        row_check, col_check, box_check = None, None, None
        if ((new_row,new_col)) in mapping:
            box_check = True
        else:
            seen = set()
            for i in range(new_row, new_row+3):
                for j in range(new_col,new_col+3):
                    if board[i][j]==".":
                        continue
                    if board[i][j] in seen:
                        return False
                    else:

                        seen.add(board[i][j])

            mapping[(new_row, new_col)]=True

        if row in mapping:
            row_check= True

        else:
            seen = set()
            for i in range(9):
                if board[row][i]==".":
                    continue
                if board[row][i] in seen:
                    return False
                else:

                    seen.add(board[row][i])
            mapping[row]=True

        if col in mapping_col:
            col_check= True

        else:
            seen = set()
            for i in range(9):
                if board[i][col]==".":
                    continue
                if board[i][col] in seen:
                    return False
                else:

                    seen.add(board[i][col])
            mapping_col[col]=True

        return True

        
        

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        mapping_box={}
        mapping = {}
        for i in range(9):
            for j in range(9):

                if not self.check(i,j,board,mapping_box, mapping):
                    return False

        return True

        