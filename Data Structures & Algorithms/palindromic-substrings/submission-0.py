class Solution:
    def solve(self, s, l, r, n, ans):

        while l>=0 and r<n and s[l]==s[r]:
            ans[0]+=1
            l-=1
            r+=1

        return s[l+1:r]

    def countSubstrings(self, s: str) -> int:
        ans = [0]    
        n = len(s)
        for i in range(n):
            self.solve(s, i,i, n, ans)
            self.solve(s, i, i+1, n, ans)

        return ans[0]