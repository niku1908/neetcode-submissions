# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, root, max_value):

        if not root:
            return 0
        
        if root.val>=max_value:
            left = self.solve(root.left, root.val)
            right = self.solve(root.right, root.val)

            return 1+left+right
        else:
            left = self.solve(root.left, max_value)
            right = self.solve(root.right, max_value)

            return left+right

    def goodNodes(self, root: TreeNode) -> int:
        
        return self.solve(root, -101)