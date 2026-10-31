class Solution:
    def solve(self,nums,curr,prev,dp):
        if curr>=len(nums):
            return 0

        if dp[curr][prev+1]!=-1:
            return dp[curr][prev+1]
        a, b = 0, 0
        if prev==-1:
            a = 1+self.solve(nums, curr+1, curr,dp)
            b = self.solve(nums,curr+1, prev,dp)
        else:
            if nums[curr]>nums[prev]:
                a = 1+self.solve(nums, curr+1, curr,dp)
            b = self.solve(nums, curr+1, prev,dp)
        
        dp[curr][prev+1]= max(a,b)
        return dp[curr][prev+1]

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[-1 for i in range(len(nums)+2)] for i in range(len(nums)+1)]
        return self.solve(nums, 0,-1,dp)