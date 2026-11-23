class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if sum(nums)<target:
            return 0
        
        min_len = float('inf')

        j = 0
        i = 0
        total = 0
        while j<len(nums):
            total+=nums[j]

            while i<=j and total>=target :
                min_len = min(min_len, j-i+1)
                total-=nums[i]
                i+=1

            j+=1
        if min_len == float('inf'):
            return 0
        return min_len

