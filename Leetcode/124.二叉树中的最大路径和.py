# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('-inf')

        def helper(root):
            if not root:
                return 0
            # 左边最大值
            left = helper(root.left)
            # 右边最大值
            right = helper(root.right)
            # 和全局变量比较
            self.res = max(left + right + root.val, self.res)
            # >0 说明都能使路径变大
            return max(0, max(left, right) + root.val)

        helper(root)
        return self.res


if __name__ == '__main__':
    S = Solution()
    root = TreeNode(3)
    node1 = TreeNode(9)
    node2 = TreeNode(20)
    node3 = TreeNode(15)
    node4 = TreeNode(7)
    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4
    print(S.maxPathSum(root))
