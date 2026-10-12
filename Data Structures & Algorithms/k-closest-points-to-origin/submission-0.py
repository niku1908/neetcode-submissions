class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        import heapq
        pq = []
        for i,j in points:
            dis = pow(pow(i,2)+pow(j,2), 0.5)

            heapq.heappush(pq, (dis,i,j))

        ans = []

        while pq:
            k-=1
            x,y,z = heapq.heappop(pq)
            ans.append([y,z])
            if k==0:
                break

        return ans