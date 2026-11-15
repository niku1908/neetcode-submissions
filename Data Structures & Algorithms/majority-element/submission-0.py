class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        target = len(nums)//2
        mapping = {}
        for i in nums:
            if i in mapping:
                mapping[i]+=1
            else:
                mapping[i]=1

            if mapping[i]>target:
                return i