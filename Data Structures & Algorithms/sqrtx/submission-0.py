class Solution:
    def mySqrt(self, x: int) -> int:
        
        i = 0
        j = x

        while i<=j:
            mid = (i+j)//2

            product = mid*mid

            if product==x:
                return mid

            elif product>x:
                j = mid-1

            else:
                i = mid+1

        return j