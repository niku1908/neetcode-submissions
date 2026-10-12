class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        import heapq
        pq = []

        for i in nums:

            heapq.heappush(pq, i)
            
            if len(pq)>k:
                heapq.heappop(pq)


        return pq[0]