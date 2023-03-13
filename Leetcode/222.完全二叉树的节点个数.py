class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if not root.left and not root.right:
            return 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

