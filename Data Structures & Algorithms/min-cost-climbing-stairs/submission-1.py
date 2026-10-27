class Solution:
    
    def solve(self, cost, index, n,dp):
        
        if index>n:
            return float('inf')
        if index==n:
            return 0
        if index==n-1:
            return cost[index]

        if dp[index]!=-1:
            return dp[index]

        a = cost[index]+self.solve(cost, index+1, n,dp)
        b = cost[index]+self.solve(cost, index+2,n,dp)
        # c = self.solve(cost, index+1, n)

        dp[index] = min(a,b)
        return dp[index]
        

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        if n<2:
            return 0
        dp = [-1 for i in range(len(cost)+1)]
        return min(self.solve(cost, 0, n,dp), self.solve(cost, 1, n,dp))
        