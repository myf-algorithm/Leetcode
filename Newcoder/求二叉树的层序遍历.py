# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类
# @return int整型一维数组
#
class Solution:
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root):
        # write code here
        if root is None:
            return self.res
        self.pre_order(root)
        return self.res

    def pre_order(self, root):
        if root is None:
            return
        self.res.append(root.val)
        self.pre_order(root.left)
        self.pre_order(root.right)


class Solution_1:
    def preorderTraversal(self, root):
        if not root:
            return []
        queue = []
        res = []
        node = root
        while queue or node:
            while node:
                queue.append(node)
                res.append(node.val)
                node = node.left

            node = queue.pop()
            node = node.right
        return res
