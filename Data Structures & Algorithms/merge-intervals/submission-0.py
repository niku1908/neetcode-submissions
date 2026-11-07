class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        intervals.sort()
        ans =[intervals[0]]

        for i in range(1, len(intervals)):
            x,y = intervals[i]
            a,b = ans[-1]

            if a<=x<=b:
                ans[-1]=[a,max(y,b)]
            else:
                ans.append(intervals[i])

        return ans