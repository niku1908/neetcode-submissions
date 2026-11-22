class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        arr = []
        
        for i in nums:
            if i in arr:
                continue
            
            arr.append(i)

        for i in range(len(arr)):
            nums[i] = arr[i]

        return len(arr)