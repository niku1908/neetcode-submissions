class Solution:

    def encode(self, strs: List[str]) -> str:

        ans = ""
        for i in strs:
            ans+=f"{len(i)}"
            ans+='#'
            ans+=i

        return ans

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i <len(s):
            j = i
            while s[j]!='#':
                j+=1

            length = int(s[i:j])

            string = s[j+1:j+1+length]

            res.append(string)

            i= j+1+length


        return res
