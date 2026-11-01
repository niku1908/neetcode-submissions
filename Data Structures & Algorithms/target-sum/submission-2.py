class Solution:
    def solve(self, nums, index, target, total,dp):
        if index==len(nums) and total == target:
            return 1

        if index>=len(nums):
            return 0
        if (index,total) in dp:
            return dp[(index,total)]

        a = self.solve(nums,index+1, target, total+nums[index],dp)
        b = self.solve(nums, index+1, target, total-nums[index],dp)

        dp[(index,total)] = a+b
        
        return dp[(index,total)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        return self.solve(nums, 0, target, 0,dp)