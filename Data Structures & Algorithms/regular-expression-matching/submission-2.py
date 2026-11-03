class Solution:
    def solve(self, s, p, i, j,dp):
        # CHANGE 1: Base case ko change kiya taaki agar string pehle khatam ho jaye, 
        # toh bacha hua pattern (jaise a*b*) sahi se check ho sake.
        if j >= len(p):
            return i >= len(s)
        
        # CHANGE 2: Ek safety check lagaya ki i string ke andar hi rahe
        first_match = i < len(s) and (p[j] == '.' or s[i] == p[j])
        if (i,j) in dp:
            return dp[(i,j)]
        ans = None
        # CHANGE 3: Pehle character par khade hokar agle character (j+1) par '*' check kiya
        if j + 1 < len(p) and p[j+1] == '*':
            ans = self.solve(s, p, i, j+2,dp) or (first_match and self.solve(s, p, i+1, j,dp))

        elif first_match:
            ans = self.solve(s, p, i+1, j+1,dp)

        else:
            ans = False

        dp[(i,j)] = ans
        return dp[(i,j)]

    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        return self.solve(s, p, 0, 0,dp)
