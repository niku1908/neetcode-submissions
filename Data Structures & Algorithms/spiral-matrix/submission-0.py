class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        row_end = len(matrix)
        row_start = 0
        col_start = 0
        col_end = len(matrix[0])

        ans = []

        while row_start<row_end and col_start<col_end:

            for i in range(col_start, col_end):
                ans.append(matrix[row_start][i])

            row_start+=1

            for i in range(row_start, row_end):
                ans.append(matrix[i][col_end-1])

            col_end-=1
            if row_start<row_end:
                for i in range(col_end-1, col_start-1,-1):
                    ans.append(matrix[row_end-1][i])

                row_end-=1

            if col_start<col_end:
                for i in range(row_end-1, row_start-1, -1):
                    ans.append(matrix[i][col_start])

                col_start+=1
            # print(ans)


        return ans