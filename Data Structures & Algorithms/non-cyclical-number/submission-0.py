class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n:

            string = str(n)
            total = 0
            for i in string:
                total+=(pow(int(i),2))

            if total == 1:
                return True
            if total in seen:
                return False
            seen.add(total)
            n = total