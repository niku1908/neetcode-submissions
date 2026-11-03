class Solution:
    def solve(self, nums , index,dp):
        if index==len(nums)-1:
            return True
        if index in dp:
            return dp[index]

        for i in range(1,nums[index]+1):
            if self.solve(nums, i+index,dp):
                dp[index] = True
                return dp[index]

        dp[index] = False
        return dp[index]

    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        return self.solve(nums, 0,dp)