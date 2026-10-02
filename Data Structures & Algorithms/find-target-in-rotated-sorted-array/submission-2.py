class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        n = len(nums)
        j = n-1
        
        while(i<=j):
            mid = (i+j)//2
            if target==nums[mid]:
                return mid
            if nums[i]<=nums[mid]:
                if nums[i]<=target<nums[mid]:
                    j = mid-1
                else:
                    i =mid+1
                
            else:
                if nums[mid]<target<=nums[j]:
                    i = mid+1
                else:
                    j = mid-1

        return -1