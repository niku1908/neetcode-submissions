class Solution:

    def solve(self, nums, target, index, ans,temp):

        if target==0:
            # if temp not in ans:
            ans.append(temp.copy())
            return

        if target<0 or index>=len(nums):
            return 

        self.solve(nums,target, index+1, ans, temp)

        temp.append(nums[index])
        # self.solve(nums, target-nums[index], index+1, ans, temp)
        self.solve(nums,target-nums[index], index, ans, temp)
        temp.pop()


    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans =[]
        self.solve(nums, target, 0, ans,[])
        return ans