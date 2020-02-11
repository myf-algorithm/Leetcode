# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        递归，中序遍历
        """
        self.res, self.count = None, k

        def inorder(root):
            if not (root and self.count):
                return
            inorder(root.left)
            self.count -= 1
            if not self.count:
                self.res = root.val
            inorder(root.right)

        inorder(root)
        return self.res

    def kthSmallest1(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        迭代方法
        """
        cur = root
        stack = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            tmp = stack.pop()
            k -= 1
            if k == 0:
                return tmp.val
            if tmp.right:
                cur = tmp.right
