class Solution:

    def solve(self, ans,mapping,digits,index,string):
        if index>=len(digits):
            ans.append(string[:])
            return

        digit_string = mapping[digits[index]]
        for i in range(len(digit_string)):
            string+=digit_string[i]
            self.solve(ans, mapping,digits, index+1, string)
            string = string[:-1]



    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        mapping = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        ans = []
        self.solve(ans,mapping, digits,0,"")
        return ans