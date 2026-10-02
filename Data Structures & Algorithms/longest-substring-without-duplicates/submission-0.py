class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        seen = set()
        ans = 0
        n = len(s)
        while i<n and j<n:

            if s[j] not in seen:
                seen.add(s[j])
                j+=1

            else:
                while s[i]!=s[j]:
                    seen.remove(s[i])
                    i+=1
                i+=1
                j+=1

            ans = max(ans, j-i)

        return ans