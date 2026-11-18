class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapping = {}
        mapping[0]=1

        curr_sum = 0
        ans = 0
        for i in nums:
            curr_sum += i
            if (curr_sum-k) in mapping:
                ans+=mapping[curr_sum-k]

            if curr_sum in mapping:
                mapping[curr_sum]+=1
            else:
                mapping[curr_sum]=1

        return ans