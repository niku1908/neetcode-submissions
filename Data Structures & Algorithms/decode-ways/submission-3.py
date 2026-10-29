class Solution:
    def solve(self, s, index,dp):
        if index>=len(s):
            return 1

        if dp[index]!=-1:
            return dp[index]
        ans = 0
        for i in range(index, len(s)):
            
            string  = s[index:i+1]
            if string[0]=='0':
                return 0
            dig = int(string)
            if dig>=1 and dig<27:
                ans+=self.solve( s, i+1,dp)

        dp[index] = ans
        return dp[index]

    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0
        dp = [-1 for i in range(len(s)+1)]
        # ans = [0]

        return self.solve( s,0,dp)
        # return ans[0]