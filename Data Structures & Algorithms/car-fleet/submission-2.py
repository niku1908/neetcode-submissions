class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = -1
        ans = 0
        pair = []
        for i in range(len(position)):
            x = round(((target-position[i])/speed[i]),2)

            pair.append((position[i],x))

        pair.sort(reverse = True)

        for i,j in pair:
            if stack==-1:
                stack = j
                ans+=1
            else:
                if j<=stack:
                    continue
                else:
                    ans+=1
                    stack =j

        return ans
                
            



            