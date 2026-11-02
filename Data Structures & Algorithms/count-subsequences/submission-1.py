class Solution:

    def solve(self, s, t, i, j,dp):
        if j==len(t):
            return 1

        if i>=len(s):
            return 0

        if (i,j) in dp:
            return dp[(i,j)]

        ans = 0
        if s[i]==t[j]:
            ans = self.solve(s,t,i+1,j+1,dp)
        ans+=self.solve(s,t,i+1,j,dp)

        dp[(i,j)]= ans
        return dp[(i,j)]



    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        return self.solve(s, t, 0,0,dp)