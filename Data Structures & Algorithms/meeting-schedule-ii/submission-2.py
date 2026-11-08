"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda i:i.start)
        
        room_heap = []
        heapq.heappush(room_heap, intervals[0].end)

        for i in range(1, len(intervals)):
            if intervals[i].start>=room_heap[0]:
                heapq.heappop(room_heap)

            heapq.heappush(room_heap, intervals[i].end)

        return len(room_heap)
            

