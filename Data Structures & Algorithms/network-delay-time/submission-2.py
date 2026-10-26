class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, x: int) -> int:
        
        q = deque()
        mapping ={i:[] for i in range(n+1)}

        for i,j,k in times:
            mapping[i].append((j,k))

        q.append((x,0))
        seen = set()
        ans = -1
        dis = [float('inf')]*(n+1)
        while q:
            
            src, time = q.popleft()
            if dis[src]>time:
                dis[src]=time
            else:
                continue
            seen.add(src)

            if len(seen)==n:
                ans = max(dis[1:])
            # print(src, time, dis, seen, ans)
            for i,j in mapping[src]:
                q.append((i,j+time))

        return ans
