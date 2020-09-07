class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
#
# @param root TreeNode类 the root
# @return int整型一维数组
#
class Solution:
    def __init__(self):
        self.res = []

    def findError(self , root ):
        # write code here
        if not root:
            return self.res
        self.inorder(root)
        res = self.res
        new_res = sorted(res)
        output = []
        for i in range(len(res)):
            if res[i] != new_res[i]:
                output.append(new_res[i])
        return output

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)
