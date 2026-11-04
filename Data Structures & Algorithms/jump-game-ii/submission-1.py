class Solution:

    def solve(self, nums, index,dp):
        if index == len(nums)-1:
            return 0
        if index>=len(nums):
            return -1

        if dp[index]!=-1:
            return dp[index]

        ans = float('inf')
        for i in range(1, nums[index]+1):
            if index+i<len(nums):
                ans = min(ans, 1+self.solve(nums, i+index,dp))

        dp[index] = ans
        return dp[index]

    def jump(self, nums: List[int]) -> int:
        dp = [-1 for i in range(len(nums)+1)]
        return self.solve(nums, 0,dp)