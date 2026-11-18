class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        ans = []
        mapping = {}
        target = len(nums)//3

        for i in nums:
            if i in ans:
                continue
            if i in mapping:
                mapping[i]+=1
            else:
                mapping[i]=1

            if mapping[i]>target:
                ans.append(i)

        return ans