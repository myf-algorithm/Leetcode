class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
#
# @param num int整型一维数组
# @return TreeNode类
#
class Solution:
    def sortedArrayToBST(self, num):
        # write code here
        if not num:
            return

        mid = int(len(num) // 2)

        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid + 1:])

        return root
