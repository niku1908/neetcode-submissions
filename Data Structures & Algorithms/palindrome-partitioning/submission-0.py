class Solution:
    def check(self, string):
        # print(string)
        i = 0
        j = len(string)-1

        while i<=j:
            if string[i]!=string[j]:
                return False

            i+=1
            j-=1

        return True

    def solve(self, ans, s, index,temp):
        n = len(s)
        if index>=n:
            ans.append(temp.copy())
            return

        for i in range(index+1, n+1):
            string = s[index:i]
            if self.check(string):
                temp.append(string)
                self.solve(ans, s, i,temp)
                temp.pop()
            


    def partition(self, s: str) -> List[List[str]]:
        
        ans = []
        self.solve(ans, s, 0,[])
        return ans