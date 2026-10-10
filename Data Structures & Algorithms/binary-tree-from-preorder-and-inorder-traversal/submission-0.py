# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def solve(self, preIndex, preorder, mini, maxi, mapping):
        if mini>maxi:
            # preIndex[0]-=1
            return None
        ele = preorder[preIndex[0]]
        new_node = TreeNode(ele)
        preIndex[0]+=1

        inorder_index = mapping[ele]

        
        new_node.left = self.solve(preIndex, preorder, mini, inorder_index-1, mapping)

        new_node.right = self.solve(preIndex, preorder, inorder_index+1, maxi, mapping)

        return new_node

        

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIndex = [0]
        mapping = {}
        for i in range(len(inorder)):
            mapping[inorder[i]]=i
        return self.solve(preIndex, preorder, 0 , len(preorder)-1, mapping)















