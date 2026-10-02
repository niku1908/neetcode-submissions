class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []

        n = len(nums)
        i = 0
        j = 1
        k = n-1

        while(i<n):
            j = i+1
            k = n-1
            while(j<k):
                total = nums[i]+nums[j]+nums[k]
                if total<0:
                    j+=1
                elif total>0:
                    k-=1
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()
                    if temp not in ans:
                        ans.append(temp)
                    j+=1
                    k-=1
            i+=1

        return ans