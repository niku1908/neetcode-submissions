class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            remainder = n%2
            if remainder == 1:
                count+=1
            n = n//2
            if n==0:
                return count
        return count
