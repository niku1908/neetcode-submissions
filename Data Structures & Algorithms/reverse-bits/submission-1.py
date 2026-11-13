class Solution:
    def reverseBits(self, n: int) -> int:
        
        num = ""
        while n:
            remainder = n%2
            num+=(str(remainder))
            n = n//2
            if n==0:
                break

        rev_string = num

        while len(rev_string)!=32:
            rev_string+=(str(0))


        # print(rev_string)

        index = 0

        result = 0

        for i in range(32):
            output = int(rev_string[31-i])*(pow(2,i))
            result+=output

        return result