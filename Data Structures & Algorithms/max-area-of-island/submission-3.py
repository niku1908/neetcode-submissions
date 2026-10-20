class Solution:

    def solve(self, grid, row, col, i, j):
        if i<0 or j<0 or i>=row or j>=col or grid[i][j]!=1:
            
            return 0

        grid[i][j]=-1

        a = self.solve(grid, row, col, i+1, j)
        b = self.solve(grid, row, col, i-1, j)
        c = self.solve(grid, row, col, i, j+1)
        d = self.solve(grid, row, col, i, j-1)

        return 1+a+b+c+d

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ans = [0]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    
                    area = self.solve(grid, len(grid), len(grid[0]), i, j)  
                    ans[0]=max(ans[0], area)

        return ans[0]