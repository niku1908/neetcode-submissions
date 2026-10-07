# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from queue import deque
        q = deque()
        ans =[]
        q.append(root)

        while q:
            temp =[]
            size = len(q)
            while size:
                x = q.popleft()
                if x.left is not None:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
                temp.append(x.val)
                size-=1
            ans.append(temp)
        return ans
                
