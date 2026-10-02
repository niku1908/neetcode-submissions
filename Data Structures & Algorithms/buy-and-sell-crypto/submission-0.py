class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        mini = prices[0]
        for i in range(1,len(prices)):
            mini = min(mini, prices[i])

            ans = max(ans, prices[i]-mini)

        return ans