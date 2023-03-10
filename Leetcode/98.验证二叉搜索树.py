# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(root, min_node, max_node):
            # base case
            if root is None:
                return True
            # 如果 root.val 不满足 max 和 min 的限制，说明不是合法的bst
            if (min_node is not None) and (root.val <= min_node.val):
                return False
            if (max_node is not None) and (root.val >= max_node.val):
                return False
            # 限定左子树的最大值是 root.val，右子树的最小值是 root.val
            return traverse(root.left, min_node, root) and traverse(root.right, root, max_node)

        return traverse(root, None, None)


if __name__ == '__main__':
    S = Solution()
    root = TreeNode(5)
    node1 = TreeNode(3)
    node2 = TreeNode(6)
    node3 = TreeNode(1)
    node4 = TreeNode(4)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    print(S.isValidBST1(root))
