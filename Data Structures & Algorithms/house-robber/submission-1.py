class Solution:

    def solve(self, nums, index, n,dp):

        if index>=n:
            return 0
        if dp[index]!=-1:
            return dp[index]
        
        a = self.solve(nums, index+1, n, dp)
        b = nums[index]+self.solve(nums, index+2, n,dp)

        dp[index] = max(a,b)
        return dp[index]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for i in range(n+1)]
        return max(self.solve(nums, 0, n,dp), self.solve(nums, 1, n,dp)) 