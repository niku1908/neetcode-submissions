"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # intervals.sort()
        # print(type(intervals[0]))
        intervals.sort(key = lambda i:i.start)
        for i in range(1,len(intervals)):
            x,y = intervals[i].start, intervals[i].end
            a,b = intervals[i-1].start, intervals[i-1].end

            if x<b:
                return False

        return True

