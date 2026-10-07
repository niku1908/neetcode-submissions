# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def check(self,root, subroot):

        if not root and not subroot:
            return True

        if root and subroot:
            return root.val==subroot.val and self.check(root.left, subroot.left) and self.check(root.right, subroot.right)

        return False

    def solve(self, root, subroot):

        if root and subroot:
            if root.val == subroot.val:
                if self.check(root, subroot):
                    return True
        elif not root and not subroot:
            return True
        else:
            return False
        
        
        left = self.solve(root.left, subroot)
        right = self.solve(root.right,subroot)

        if left or right:
            return True
        return False


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        return self.solve(root, subRoot)