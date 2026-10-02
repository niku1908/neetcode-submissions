class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        i = 0
        n = len(nums)
        j = n-1
        ans = float('inf')
        while(i<=j):
            mid = (i+j)//2
            ans = min(ans, nums[mid])
            if nums[j]<nums[mid]:
                i = mid+1
            else:
                j =mid-1

        return ans
