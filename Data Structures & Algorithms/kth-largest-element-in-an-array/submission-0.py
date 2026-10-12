class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        import heapq
        pq = []

        for i in nums:

            heapq.heappush(pq, -i)
            
            
        while pq:
            k-=1
            x = heapq.heappop(pq)
            if k==0:
                return -x


        # return pq[0]