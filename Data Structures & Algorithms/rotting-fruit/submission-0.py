class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        fresh=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j,0))

        time = 0
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]
        temp = 0
        while q:
            x,y,z = q.popleft()
            time = max(time, z)
            
            for i, j in zip(dx,dy):
                nx = i+x
                ny = j+y

                if nx>=0 and ny>=0 and nx<len(grid) and ny<len(grid[0]) and grid[nx][ny]==1:
                    temp+=1
                    grid[nx][ny]=2
                    q.append((nx,ny, z+1))
                    
                
        if temp!=fresh:
            return -1


        return time








