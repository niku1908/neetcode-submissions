class Solution:
    def solve(self, nums, index, n,dp):

        if index>=n:
            return 0
        if dp[index]!=-1:
            return dp[index]

        a = nums[index]+self.solve(nums, index+2, n,dp)
        b = self.solve(nums, index+1,n,dp)

        dp[index] = max(a,b)
        return dp[index]

    def rob(self, nums: List[int]) -> int:
        
        dp1 =[-1 for i in range(len(nums)+1)]
        dp2 =[-1 for i in range(len(nums)+1)]
        n = len(nums)
        if n<3:
            return max(nums)
        return max(self.solve(nums, 0, n-1,dp1), self.solve(nums, 1, n,dp2))