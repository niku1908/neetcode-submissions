class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows = len(board)
        cols = len(board[0])
        q = deque()
        
        for row in range(0, rows):
            if board[row][0]=="O":
                q.append((row, 0))
            if board[row][cols-1]=="O":
                q.append((row, cols-1))

        for col in range(0, cols):
            if board[0][col]=="O":
                q.append((0, col))

            if board[rows-1][col]=="O":
                q.append((rows-1, col))
        seen = set()
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]
        while q:
            x,y = q.popleft()
            seen.add((x,y))
            for i,j in zip(dx,dy):
                nx = i+x
                ny = j+y

                if nx>=0 and ny>=0 and nx<rows and ny<cols and (nx,ny) not in seen and board[nx][ny]=="O":
                    q.append((nx,ny))

        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="O" and (i,j) not in seen:
                    board[i][j]="X"
       
