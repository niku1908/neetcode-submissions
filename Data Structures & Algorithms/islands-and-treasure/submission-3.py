class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
       
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j]==0:
                    q.append((i,j,0))
                    

        dx = [-1,1,0,0]
        dy = [0,0,1,-1]

        while q:
            x,y,z = q.popleft()
            for i,j in zip(dx,dy):
                nx = i+x
                ny = j+y
                if nx>=0 and ny>=0 and nx<len(grid) and ny<len(grid[0]):
                    if grid[nx][ny]==2147483647:
                        grid[nx][ny]=(z+1)
                        q.append((nx,ny,(z+1)))









