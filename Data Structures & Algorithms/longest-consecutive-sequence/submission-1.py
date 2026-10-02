class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 1
        mapping = {}

        nums.sort()
        n = len(nums)

        for i in range(n):
            if (nums[i]-1) in mapping:
                ans = max(ans, mapping[nums[i]-1]+1)

                mapping[nums[i]]=mapping[nums[i]-1]+1
            else:
                mapping[nums[i]]=1

        return ans