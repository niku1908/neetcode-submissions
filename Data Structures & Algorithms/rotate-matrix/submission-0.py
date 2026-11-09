class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        i, j = 0, len(matrix)-1

        while i<=j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i+=1
            j-=1

        seen = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(i,j)
                if i==j:
                    continue
                if (i,j) not in seen:
                    seen.add((i,j))
                    seen.add((j,i))
                    matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]

