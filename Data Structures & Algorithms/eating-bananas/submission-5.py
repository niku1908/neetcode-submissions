class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:      
        maxi = max(piles)
        

        i = 1
        j = maxi
        ans = maxi
        while(i<=j):
            mid = (i+j)//2
            count = 0
            for pile in piles:
                count+=(pile+mid-1)//mid
                
                
            if count<=h:
                ans = mid
                j = mid-1
            else:
                i = mid+1

        return ans

            
            

        