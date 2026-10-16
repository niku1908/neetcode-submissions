class Solution:

    def solve(self, ans, n, open, close, temp,pair):
        if open==n and close==n and pair==n:
            # print(temp)
            ans.append(temp[:])
            return

        if open>n or close>n or close>open or pair>n:
            return

        
        temp+="("
        self.solve(ans, n, open+1, close, temp, pair)
        temp = temp[:-1]
        
        temp+=")"
        self.solve(ans, n, open, close+1, temp, pair+1)
        temp = temp[:-1]



    def generateParenthesis(self, n: int) -> List[str]:
        
        ans =[]
        self.solve(ans, n, 0,0,"",0)
        return ans