class Solution:
    def checkValidString(self, s: str) -> bool:
        cmax, cmin = 0,0
        for i in s:
            if i=='(':
                cmax+=1
                cmin+=1
            elif i==')':
                cmax-=1
                cmin-=1

            elif i=='*':
                cmax+=1
                cmin-=1

            if cmax<0:
                return False

            if cmin<0:
                cmin = 0

        return cmin==0