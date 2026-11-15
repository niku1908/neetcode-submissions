class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ans = ""
        letter = -1
        while True:
            letter+=1
            if letter>=len(strs[0]):
                return ans
            to_match = strs[0][letter]
            for i in range(1,len(strs)):
                
                word = strs[i]
                if letter>=len(word):
                    return ans
                if word[letter] != to_match:
                    return ans

            ans+=to_match    
        return ans

                



            