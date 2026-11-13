class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        original = n*(n+1)/2

        total = sum(nums)

        return int(original-total)