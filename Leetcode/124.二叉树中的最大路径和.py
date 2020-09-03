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

# 关于递归地讲解：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/124di-gui-de-jing-sui-ji-lu-yi-xia-by-821218213/
# 二叉树递归算法的基础结构：
# def dfs(root):
#     if not root: return
#     dfs(root.left)
#     dfs(root.right)
# 在此基础上进行返回值，参数，外部变量的设计
# 外部变量：使用self.res来记录最大的路径值
# 递归函数的参数：只需要一个根节点遍历完二叉树就行，且最大值必须要遍历完才知道是不是最大值，只使用root
# 返回值的设计：选左右子树中较大的值，加上val，和0比较，截断为0
