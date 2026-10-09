# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def solve(self, root, mini, maxi):

        if not root:
            return True
        ans = None
        if maxi>root.val>mini:
            ans = True
        else:
            ans= False

        
        
        return ans and self.solve(root.left, mini, root.val) and self.solve(root.right, root.val, maxi)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.solve(root, float('-inf'), float('inf'))
