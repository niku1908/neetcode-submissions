class Solution:

    def solve(self, s, words, index,dp):

        if index>=len(s):
            return True
        if dp[index]!=-1:
            return dp[index]

        for i in range(index, len(s)):
            string =s[index:i+1]
            if string in words:
                if self.solve(s, words, i+1,dp):
                    dp[index] = True
                    return dp[index]
            
        dp[index] = False
        return dp[index]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [-1 for i in range(len(s)+1)]
        return self.solve(s, words,0,dp)