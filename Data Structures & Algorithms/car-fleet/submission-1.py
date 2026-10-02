class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        ans = 0
        pair = []
        for i in range(len(position)):
            x = round(((target-position[i])/speed[i]),2)

            pair.append((position[i],x))

        pair.sort(reverse = True)

        for i,j in pair:
            if not stack:
                stack.append(j)
            else:
                if j<=stack[-1]:
                    continue
                else:
                    stack.append(j)

        return len(stack)
                
            



            