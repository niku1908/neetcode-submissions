class Solution:

    def solve(self, nums, ans, temp, index):
        if index>=len(nums):
            if temp not in ans:
                ans.append(temp.copy())
            return

        temp.append(nums[index])
        self.solve(nums, ans, temp, index+1)
        temp.pop()
        old = index
        while index+1<len(nums):
            if nums[index+1]==nums[index]:
                index+=1
                continue
            else:
                break

        self.solve(nums, ans, temp, index+1)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        nums.sort()
        self.solve(nums, ans, [], 0)
        
        return ans