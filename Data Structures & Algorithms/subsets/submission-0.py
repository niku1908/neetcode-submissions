class Solution:
    def solve(self, ans, nums, i, temp):
        n = len(nums)

        if i>=n:
            ans.append(temp.copy())
            return

        
        temp.append(nums[i])
        self.solve(ans, nums, i+1, temp)
        temp.pop()
        self.solve(ans,nums, i+1,temp)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans =[]
        self.solve(ans, nums, 0,[])
        return ans