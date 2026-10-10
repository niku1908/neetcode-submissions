# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def solve(self, root, ans, k):
        # print(root.val, ans, k)
        if not root:
            return

        self.solve(root.left, ans, k)
        k[0]-=1
        if k[0]==0:
            ans[0]=root.val
        self.solve(root.right, ans, k)

        
        

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = [-1]
        count = [k]
        self.solve(root, ans,count)
        return ans[0]