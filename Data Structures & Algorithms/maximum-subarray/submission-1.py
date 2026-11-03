class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans = -float('inf')
        total = 0

        for i in nums:
            total+=i

            ans = max(ans, total)
            if total<0:
                total = 0

        return ans