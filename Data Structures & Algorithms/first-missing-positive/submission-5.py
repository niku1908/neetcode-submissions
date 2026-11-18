class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        nums = list(seen)
        nums.sort()
        j = 1
        for i in range(len(nums)):
            if nums[i]<1:
                continue
            
            if nums[i]!=j:
                return j
            else:
                j+=1

        return j
            