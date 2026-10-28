class Solution:
    def solve(self, l, r, s, n):

        while(l>=0 and r<n and s[l]==s[r]):
            l-=1
            r+=1

        return s[l+1:r]
        
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans =""
        for i in range(n):
            odd_string = self.solve(i,i, s, n)
            even_string = self.solve(i,i+1,s,n)

            if len(ans)<len(odd_string):
                ans = odd_string

            if len(even_string)>len(ans):
                ans = even_string

        return ans