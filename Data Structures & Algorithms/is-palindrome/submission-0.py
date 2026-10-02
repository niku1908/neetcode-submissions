class Solution:
    def check_char(self, s):
        if 'a'<=s<='z' or 'A'<=s<='Z' or '0'<=s<='9':
            return True

        return False
    def isPalindrome(self, s: str) -> bool:
        
        i =0
        n = len(s)
        j = n-1

        while(i<=j):
            if not self.check_char(s[i]):
                i+=1
                continue

            if not self.check_char(s[j]):
                j-=1
                continue

            if s[i].lower()!=s[j].lower():
                return False

            i+=1
            j-=1

        return True
