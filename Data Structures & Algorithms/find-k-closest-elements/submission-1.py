class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        q = deque()
        max_diff_q = None
        for i in arr:

            diff = abs(x-i)

            if max_diff_q is None:
                max_diff_q = diff
                q.append(i)
            else:
                if len(q)==k:
                    if max_diff_q>diff:
                        q.popleft()
                        q.append(i)
                        max_diff_q = abs(x-q[0])
                    
                else:
                    q.append(i)
        return list(q)