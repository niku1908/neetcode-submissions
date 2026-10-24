class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 0 not visited, 1 visiting, 2 visited
        
        state = [0]*n
        mapping = {i:[] for i in range(n)}
        parent = set()
        for i,j in edges:
            parent.add(i)
            parent.add(j)
            mapping[j].append(i)
            mapping[i].append(j)

        
        def has_cycle(node):
            
            if state[node]==1:
                return True

            if state[node]==2:
                return False

            state[node]=1
            for child in mapping[node]:
                if state[child]==1:
                    continue
                if state[child]==2:
                    return True
                if has_cycle(child):
                    return True

            state[node]=2
            return False
        flag = False
        for i in range(n):
            if flag==True and i in parent and state[i]==0:
                return False
            if i in parent:
                flag = True
            if has_cycle(i):
                return False

        return True





