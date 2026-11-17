class Solution:

    def solve(self, prices, index,buy,dp):

        if index>=len(prices):
            return 0
        if (index, buy) in dp:
            return dp[(index, buy)]

        a,b = 0,0
        if buy:
            a = -prices[index]+self.solve(prices, index+1, 0,dp)
            b = self.solve(prices, index+1, 1,dp)

        else:
            a = prices[index]+self.solve(prices, index+1, 1,dp)
            b = self.solve(prices, index+1, 0,dp)

        dp[(index, buy)] = max(a,b)
        return dp[(index, buy)]

    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        return self.solve(prices, 0,1,dp)