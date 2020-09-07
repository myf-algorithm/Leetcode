class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
#
# @param root TreeNode¿‡
# @return int’˚–Õ
#
class Solution:
    def sumNumbers(self, root):
        # write code here
        tmp = 0
        res = []
        self.dfs(root, tmp, res)
        return sum(res)

    def dfs(self, root, tmp, res):
        if not root:
            return
        if not root.left and not root.right:
            res.append(tmp * 10 + root.val)
        self.dfs(root.left, tmp * 10 + root.val, res)
        self.dfs(root.right, tmp * 10 + root.val, res)
