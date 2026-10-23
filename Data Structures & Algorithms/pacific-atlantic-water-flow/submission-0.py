class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited = set()
        paci = deque()
        atla = deque()
        

        rows = len(heights)
        cols = len(heights[0])

        for col in range(0, cols):
            # heights[rows-1][col]=-1
            atla.append((rows-1, col))
            # visited.add((rows-1, col))
        
        for row in range(0, rows-1):
            # heights[row][cols-1]=-1
            atla.append((row, cols-1))

        for row in range(0, rows):
            # heights[row][0]=-1
            paci.append((row,0))

        for col in range(1, cols):
            # heights[0][col]=-1
            paci.append((0,col))
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]
        atla_final=[]
        while atla:
            x,y = atla.popleft()
            visited.add((x,y))
            atla_final.append((x,y))
            for i,j in zip(dx, dy):
                nx = x+i
                ny = y+j

                if nx>=0 and ny>=0 and nx<rows and ny<cols and (nx,ny) not in visited and heights[nx][ny]>=heights[x][y]:
                    # heights[nx][ny]=-1
                    atla.append((nx,ny))
        visited = set()
        paci_final=[]
        while paci:
            x,y = paci.popleft()
            visited.add((x,y))
            paci_final.append((x,y))
            for i,j in zip(dx, dy):
                nx = x+i
                ny = y+j

                if nx>=0 and ny>=0 and nx<rows and ny<cols and (nx,ny) not in visited and heights[nx][ny]>=heights[x][y]:
                    # heights[nx][ny]=-1
                    paci.append((nx,ny))
        # print(atla_final)
        # print(paci_final)
        ans = []
        for x in atla_final:
            if x in paci_final:
                ans.append(x)
        
        result = set(ans)
        return list(result)
        


