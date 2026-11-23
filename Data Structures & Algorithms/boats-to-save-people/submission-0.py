class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j= len(people)-1
        ans = 0
        while i<=j:

            total = people[i]+people[j]

            if total<=limit:
                ans+=1
                i+=1
                j-=1

            else:
                ans+=1
                j-=1

        return ans
