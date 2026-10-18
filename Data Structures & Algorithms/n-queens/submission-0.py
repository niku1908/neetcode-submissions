class Solution:
    def check(self,board,col, row,n):

        for i in range(n):
            if board[i][col]=='Q':
                return False
            if board[row][i]=='Q':
                return False

        i = row
        j = col
        while i>=0 and j>=0:
            if board[i][j]=='Q':
                return False

            i-=1
            j-=1

        i = row
        j = col
        while(i>=0 and j<n):
            if board[i][j]=='Q':
                return False

            i-=1
            j+=1

        return True

    def solve(self, n, board, ans,row):

        if row>=n:
            temp = []
            for i in board:
                result = "".join(i)
                temp.append(result)
            ans.append(temp)
            return

        for i in range(n):
            if self.check(board, i, row,n):
                board[row][i]='Q'
                self.solve(n,board, ans,row+1)
                board[row][i]='.'
        



    def solveNQueens(self, n: int) -> List[List[str]]:
        
        ans =[]
        board = [["." for i in range(n)] for i in range(n)]
        # print(board)
        self.solve(n, board, ans,0)
        # print(ans)
        return ans