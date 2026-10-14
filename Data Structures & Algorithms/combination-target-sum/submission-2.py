class Solution:
    def solve(self, ans, nums, index,target, temp):

        n = len(nums)
        

        if target==0:
            if temp not in ans:
                ans.append(temp.copy())
            return

        if index>=n or target<0:
            return
        
        self.solve(ans, nums, index+1, target, temp)
        temp.append(nums[index])
        self.solve(ans, nums, index, target-nums[index], temp)
        # self.solve(ans, nums,index+1, target-nums[index], temp)
        temp.pop()
        # self.solve(ans, nums, index, target,temp)



    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans =[]
        self.solve(ans, nums, 0,target, [])
        return ans