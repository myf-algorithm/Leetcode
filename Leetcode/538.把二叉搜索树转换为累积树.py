# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0

    def inorder(self, root):
        if root is None:
            return None
        self.inorder(root.right)
        self.sum += root.val
        root.val = self.sum
        self.inorder(root.left)

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.inorder(root)
        return root