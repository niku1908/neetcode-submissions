class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}
        for i in nums:
            if i in mapping:
                mapping[i]+=1
            else:
                mapping[i]=1
        ans =[]
        for i, j in mapping.items():
            ans.append((j,i))

        ans.sort(reverse=True)
        result = []
        count = 0
        for i,j in ans:
            if count==k:
                break
            count+=1
            result.append(j)



        return result