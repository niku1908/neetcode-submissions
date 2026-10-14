class MedianFinder:

    def __init__(self):
        self.lower=[]
        self.higher=[]

    def addNum(self, num: int) -> None:
        import heapq
        heapq.heappush(self.lower, -num)
        heapq.heappush(self.higher, -heapq.heappop(self.lower))

        if len(self.higher)>len(self.lower):
            heapq.heappush(self.lower, - heapq.heappop(self.higher))

    def findMedian(self) -> float:
        m = -self.lower[0]
        n = self.higher[0] if self.higher else 0

        if len(self.lower)==len(self.higher):
            return (m+n)/2

        return m


        