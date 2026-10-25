class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        visited=[0]*(len(edges)+1)
        parent = [-1 for i in range(len(edges)+1)]
        ans = None
        compo = 0
        mapping = {}
        for i,j in edges:
            if visited[i] and visited[j] and (parent[i]==parent[j]):
                
                return  [i,j]

            visited[i]=1
            
            visited[j]=1

            if parent[i]==-1 and parent[j]==-1:
                if compo in mapping:
                    mapping[compo].append(i)
                    mapping[compo].append(j)
                else:
                    mapping[compo]=[i,j]
                parent[i], parent[j]=compo, compo
                compo+=1
            elif parent[i]!=-1 and parent[j]==-1:
                
                mapping[parent[i]].append(j)
                parent[j]=parent[i]
            elif parent[i]==-1 and parent[j]!=-1:
                mapping[parent[j]].append(i)
                parent[i]=parent[j]
            else:
                p_j = parent[j]
                for ele in mapping[parent[j]].copy():
                    parent[ele]=parent[i]
                    mapping[parent[i]].append(ele)
                    
                del mapping[p_j]
                
        return ans      
        