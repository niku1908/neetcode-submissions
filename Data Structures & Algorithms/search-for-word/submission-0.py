class Solution:

    def solve(self, board, word, x,y,i,j,index, seen):
        
        if index==len(word):
            return True
        if (i,j) in seen or i>=x or i<0 or j>=y or j<0:
            return False
        a, b, c, d = False, False, False, False
        if word[index]==board[i][j]:
            
            seen.add((i,j))
            if index==len(word)-1:
                print(seen)
                return True
            a = self.solve(board, word, x,y,i+1,j,index+1, seen)
            b = self.solve(board, word, x,y,i-1,j,index+1, seen)
            c = self.solve(board, word, x,y,i,j+1,index+1, seen)
            d = self.solve(board, word, x,y,i,j-1,index+1, seen)
            seen.remove((i,j))
            return a or b or c or d
        else:
            return False

        

        

    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                seen = set()
                if self.solve(board, word, len(board),len(board[0]),i,j,0,seen):
                    return True


        return False

