class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = []
        stack = []
        temperatures.reverse()
        n = len(temperatures)
        for i in range(n):
            
            while stack and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()

            if not stack:
                ans.append(0)
                stack.append(i)
            else:

                ans.append(i-stack[-1])
                stack.append(i)
        ans.reverse()
        return ans

            

