# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = float('-inf')
        self.mapping = {}

    def max_sum(self, root):
        if root in self.mapping:
            return self.mapping[root]
        if not root:
            return 0

        left = self.max_sum(root.left)

        right = self.max_sum(root.right)
        maxi = max(left, right)
        if maxi<0:
            maxi = 0

        self.mapping[root]=root.val+maxi
        return root.val+maxi

    def pre(self, root):

        if not root:
            return

        left = self.max_sum(root.left)
        right = self.max_sum(root.right)
        if left<0:
            left = 0
        if right<0:
            right = 0
        self.ans = max(self.ans, left+right+root.val)

        self.pre(root.left)
        self.pre(root.right)


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.pre(root)

        return self.ans