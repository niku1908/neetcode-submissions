class Solution:

    def solve(self, prices, buy, index,dp):

        if index>=len(prices):
            return 0
        if dp[buy][index]!=-1:
            return dp[buy][index]
        a, b= 0, 0
        if buy:
            a = -prices[index]+self.solve(prices, 0, index+1,dp)
            b = self.solve(prices, buy, index+1,dp)

        else:
            a = prices[index]+self.solve(prices,1, index+2,dp)
            b = self.solve(prices, 0, index+1,dp)


        dp[buy][index] = max(a,b)
        return dp[buy][index]

    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1 for i in range(len(prices)+1)] for i in range(2)]
        return self.solve(prices, 1, 0,dp)