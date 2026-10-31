class Solution:
    def solve(self, m, n, i,j,dp):

        if i==m-1 and j==n-1:
            return 1

        if i>=m or j>=n or i<0 or j<0:
            return 0
        if dp[i][j]!=0:
            return dp[i][j]

        down = self.solve(m,n,i+1,j,dp)
        right = self.solve(m,n,i,j+1,dp)

        dp[i][j] = down+right
        return dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n+1)] for i in range(m+1) ]
        
        return self.solve(m,n,0,0, dp)