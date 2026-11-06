class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort()
        ans = [intervals[0]]
        # print(ans)
        for i in range(1,len(intervals)):
            x,y = intervals[i]
            a,b = ans[-1]

            if a<=x<=b:
                ans[-1]=[a,max(y,b)]
            else:
                ans.append([x,y])
            # print(ans)

        return ans
        

        