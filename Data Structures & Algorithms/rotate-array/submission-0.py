class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        arr = [-1]*len(nums)
        for i in range(len(nums)):
            pos = (i+k)%len(nums)

            arr[pos]=nums[i]

        for i in range(len(arr)):
            nums[i]=arr[i]