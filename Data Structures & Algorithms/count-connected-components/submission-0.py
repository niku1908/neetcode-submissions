class Solution:

    def solve(self, mapping, visited, node):

        if visited[node]==1:
            return

        visited[node]=1
        for i in mapping[node]:
            self.solve(mapping, visited, i)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mapping = {i:[] for i in range(n)}

        for i,j in edges:
            mapping[i].append(j)
            mapping[j].append(i)

        visited = [0]*n
        count = 0
        for i in range(n):
            if visited[i]==0:
                count+=1
                self.solve(mapping, visited, i)

        return count
            