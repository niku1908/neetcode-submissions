class Solution:

    def solve(self, grid, row, col, i,j):
        if i<0 or j<0 or i>=row or j>=col or grid[i][j]!="1":
            return

        grid[i][j]="#"

        self.solve(grid, row, col, i+1, j)
        self.solve(grid, row, col, i-1, j)
        self.solve(grid, row, col, i, j+1)
        self.solve(grid, row, col, i, j-1)



    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    count+=1
                    self.solve(grid, len(grid), len(grid[0]),i,j)
        return count