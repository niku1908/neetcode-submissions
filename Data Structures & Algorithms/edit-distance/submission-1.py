class Solution:

    def solve(self, a, b, i, j,dp):
        if j>=len(b):
            return len(a)-i
        
        if i>=len(a):
            return len(b)-j
        if (i,j) in dp:
            return dp[(i,j)]
        ans = 0
        if a[i]==b[j]:
            ans = self.solve(a,b,i+1,j+1,dp)
        else:

            x = self.solve(a,b,i,j+1,dp)
            y = self.solve(a,b,i+1,j,dp)
            z = self.solve(a,b,i+1,j+1,dp)
            ans = 1+min(x,y,z)

        dp[(i,j)] = ans
        return dp[(i,j)]

    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        return self.solve(word1, word2, 0, 0,dp)