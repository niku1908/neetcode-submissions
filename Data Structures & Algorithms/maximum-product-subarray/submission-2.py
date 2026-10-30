class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        ans, cmax, cmin = nums[0], nums[0],nums[0]

        for i in range(1, len(nums)):

            if nums[i]<0:
                cmax,cmin = cmin, cmax

            cmax = max(nums[i], cmax*nums[i])
            cmin = min(nums[i], cmin*nums[i])

            ans = max(ans, cmax)

        return ans