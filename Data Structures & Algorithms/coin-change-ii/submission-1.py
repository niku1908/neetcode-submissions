class Solution:


    def solve(self, amount, coins, index, dp):
        if amount==0:
            return 1
        if index>=len(coins) or amount<0:
            return 0
        if dp[index][amount]!=-1:
            return dp[index][amount]

        pick = self.solve(amount-coins[index],coins, index,dp)
        not_pick= self.solve(amount, coins, index+1,dp)

        dp[index][amount] = pick+not_pick
        return dp[index][amount]



    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1 for i in range(amount+1)] for i in range(len(coins)+1)]
        return self.solve(amount , coins, 0,dp)