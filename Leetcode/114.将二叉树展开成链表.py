class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 二叉树转成链表
class Solution:
    def flatten(self, root):
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)

        # 后序遍历位置
        # 1、左右子树已经被拉成一条链表
        left = root.left
        right = root.right

        # 2、将左子树作为右子树
        root.left = None
        root.right = left

        # 3、将原来的右子树拼接到当前右子树的末端
        p = root
        while p.right is not None:
            p = p.right
        p.right = right


