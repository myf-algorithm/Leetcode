# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True

        def traverse(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            return l.val == r.val and traverse(l.left, r.right) and traverse(l.right, r.left)

        return traverse(root.left, root.right)


if __name__ == '__main__':
    S = Solution()
    root = TreeNode(5)
    node1 = TreeNode(3)
    node2 = TreeNode(3)
    root.left = node1
    root.right = node2
    print(S.isSymmetric(root))
