class Solution:

    def solve(self, amount ,coins, index, dp):
        if amount==0:
            return 0

        if amount<0 or index>=len(coins):
            return float('inf')

        if dp[amount][index]!=-1:
            return dp[amount][index]
        
        a = 1+self.solve(amount-coins[index], coins, index,dp)
        b = 1+self.solve(amount-coins[index], coins, index+1,dp)
        c = self.solve(amount, coins, index+1,dp)

        dp[amount][index] = min(a,b,c)
        return dp[amount][index]

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp =[[-1 for i in range(len(coins)+1)] for i in range(amount+1)]
        ans =self.solve(amount, coins, 0,dp)
        if ans==float('inf'):
            return -1

        return ans