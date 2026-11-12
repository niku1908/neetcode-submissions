class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            num = i
            count = 0
            while num:
                remainder = num%2
                if remainder == 1:
                    count+=1

                num = num//2
                if num==0:
                    
                    break
            ans.append(count)
        return ans