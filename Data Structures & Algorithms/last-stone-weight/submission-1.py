class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        
        pq = []

        for i in stones:
            heapq.heappush(pq, -i)
        # print(pq)
        while pq:
            if len(pq)==1:
                return -pq[0]
            x = heapq.heappop(pq)
            y = heapq.heappop(pq)
            # print(x,y)

            if x==y:
                continue
            elif x<y:
                heapq.heappush(pq, x-y)
            
        return len(pq)