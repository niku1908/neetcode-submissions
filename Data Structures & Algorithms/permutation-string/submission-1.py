class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = 0
        n = len(s2)

        mapping = {}

        for ele in s1:
            if ele in mapping:
                mapping[ele]+=1
            else:
                mapping[ele]=1

        while(i<n and j<n):
            if s2[j] in mapping:
                mapping[s2[j]]-=1
                if mapping[s2[j]]==0:
                    del mapping[s2[j]]
                j+=1
            else:
                
                while(s2[i]!=s2[j]):
                    if s2[i] in mapping:
                        mapping[s2[i]]+=1
                    else:
                        mapping[s2[i]]=1
                    i+=1

                i+=1
                j+=1

            if len(mapping)==0:
                return True

        return False

                

            
