class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        for i in range(len(digits)):
            total = total*10
            total+=digits[i]

        total+=1
        ans=[]
        string = str(total)
        for i in string:
            ans.append(int(i))

        return ans