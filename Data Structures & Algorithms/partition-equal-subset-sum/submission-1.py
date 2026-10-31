class Solution:
    def solve(self, nums, target, index,dp):
        if target==0:
            return True

        if target<0 or index>=len(nums):
            return False
        
        if dp[target][index] is not None:
            return dp[target][index]

        a = self.solve(nums, target-nums[index], index+1,dp)
        b = self.solve(nums, target, index+1,dp)

        dp[target][index] = a or b
        return dp[target][index]

    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total%2!=0:
            return False
        
        target = total//2
        dp = [[None for i in range(len(nums)+1)] for i in range(target+1)]
        return self.solve(nums, target, 0,dp)