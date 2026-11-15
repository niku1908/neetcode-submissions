class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0
        n = len(nums)
        j = n-1

        while i<=j:

            if nums[i]!=val:
                i+=1
            elif nums[i]==val:
                nums[i],nums[j]=nums[j],nums[i]
                j-=1
        k = i
        # nums[:k].sort()
        return k


