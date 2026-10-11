# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root):
        result = []

        def preorder(node):
            if not node:
                result.append("#")
                return

            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(result)

    def deserialize(self, data):
        values = iter(data.split(","))

        def build_tree():
            val = next(values)

            if val == "#":
                return None

            node = TreeNode(int(val))
            node.left = build_tree()
            node.right = build_tree()

            return node

        return build_tree()