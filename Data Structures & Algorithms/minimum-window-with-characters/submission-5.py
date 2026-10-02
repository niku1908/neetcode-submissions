class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mt = {}
        for i in t:
            if i in mt:
                mt[i]+=1
            else:
                mt[i]=1

        ms = {}
        count = len(t)
        match = 0
        si = -1
        start = 0
        l = float('inf')

        for i in range(len(s)):
            if s[i] in ms:
                ms[s[i]]+=1
            else:
                ms[s[i]]=1
            if s[i] in mt:
                if ms[s[i]]<=mt[s[i]]:
                    match+=1

            while match==count:

                if l>(i-start+1):
                    l = (i-start+1)
                    si = start
                if s[start] in mt:
                    ms[s[start]]-=1
                    
                    if ms[s[start]]<mt[s[start]]:
                        match-=1

                start+=1

        if l== float('inf'):
            return ""

        return s[si:si+l]