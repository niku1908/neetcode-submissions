class Solution:
    def solve(self, matrix, rows, cols,i,j,dp):
        if (i,j) in dp:
            return dp[(i,j)]

    
        dx = [-1,1,-0,0]
        dy = [0,0,-1,1]

        ans = 1

        for x,y in zip(dx,dy):
            nx = i+x
            ny = j+y

            if  nx>=0 and ny>=0 and nx<rows and ny<cols and matrix[nx][ny]>matrix[i][j]:
                curr_len = 1+self.solve(matrix, rows, cols, nx, ny, dp)
                ans = max(ans, curr_len)
                    

                    
        dp[(i,j)]=ans
        return dp[(i,j)]


    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        ans = 0
        dp = {}
        for i in range(rows):
            for j in range(cols):
                result = 0
                result = self.solve(matrix, rows, cols , i,j,dp)
                ans = max(ans, result)

        return ans

