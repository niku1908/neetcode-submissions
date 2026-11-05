class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        mapping = {}
        for i in range(len(s)):
            if s[i] in mapping:
                mapping[s[i]][1]=i

            else:
                mapping[s[i]]=[i,i]
        array = []
        for i,j in mapping.items():
            array.append(j)
        array.sort()
        # print(array)
        
        q = deque()
        for i,j in array:
            
            if not q:
                q.append((i,j))
            else:
                
                x,y = q.pop()
                # print(x,y)
                if x<=i<=y:
                    q.append((x,max(y,j)))
                else:
                    
                    q.append((x,y))
                    q.append((i,j))
                    
        # print(q)
        result = []
        while q:
            x,y = q.popleft()
            result.append(y-x+1)

        # result.sort(reverse=True)
        return result






