class MedianFinder:

    def __init__(self):
        self.ans = []

    def addNum(self, num: int) -> None:
        self.ans.append(num)
        self.ans.sort()

    def findMedian(self) -> float:
        length = len(self.ans)
        if length%2==0:
            return (self.ans[length//2]+self.ans[(length//2)-1])/2
        return self.ans[length//2]