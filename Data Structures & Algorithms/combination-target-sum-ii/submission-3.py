class Solution:

    def solve(self,ans, candidates, index, target, temp):
        n = len(candidates)

        if target==0:
            # temp.sort()
            # if temp not in ans:

            ans.append(temp.copy())
            return

        if index>=n or target<0:
            return

        
        temp.append(candidates[index])
        self.solve(ans, candidates, index+1, target-candidates[index], temp)
        temp.pop()
        
        old = candidates[index]

        while index+1<n:
            if candidates[index+1]==candidates[index]:
                index+=1
                continue
            else:
                break
            
        self.solve(ans, candidates, index+1, target, temp)
            

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.solve(ans, candidates, 0, target, [])
        # ans.sort()
        return ans