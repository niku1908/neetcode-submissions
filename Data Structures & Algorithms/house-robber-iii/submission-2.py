# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def solve(self, root, temp,dp):

        if not root:
            return 0

        if (root, temp) in dp:
            return dp[(root, temp)]
        ans = 0
        if not temp:
            a = self.solve(root.left,1,dp)
            b = self.solve(root.right,1,dp)
            c = self.solve(root.left, 0,dp)
            d = self.solve(root.right, 0,dp)
            ans = max((root.val+a+b), (c+d))
        else:
            a = self.solve(root.left, 0,dp)
            b = self.solve(root.right, 0,dp)
            c = self.solve(root.left, 1,dp)
            d = self.solve(root.right, 1,dp)
            ans = max((a+b), (c+d))

        dp[(root, temp)] = ans
        return dp[(root,temp)]

    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}
        return self.solve(root,0,dp)