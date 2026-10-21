"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def dfs(self,root, mapping ):

        neigh = []
        clone = Node(root.val)
        mapping[root]=clone

    
        for x in root.neighbors:
            if x in mapping:
                neigh.append(mapping[x])
            else:
                neigh.append(self.dfs(x, mapping))

        clone.neighbors = neigh
        return clone

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        if not node.neighbors:
            new_node = Node(node.val, [])
            return new_node

        mapping = {}
        return self.dfs(node, mapping)
        