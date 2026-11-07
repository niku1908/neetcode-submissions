class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        previous_end = intervals[0][1]
        for i in range(1, len(intervals)):
            # print(intervals[i], previous)
            x,y = intervals[i]
            # a,b = previous

            if x<previous_end:
                ans+=1
                previous_end = min(previous_end, y)
            else:
                
                previous_end = intervals[i][1] 

        return ans