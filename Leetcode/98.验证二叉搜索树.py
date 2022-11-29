# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    假设一个二叉搜索树具有如下特征：
            节点的左子树只包含小于当前节点的数。
            节点的右子树只包含大于当前节点的数。
            所有左子树和右子树自身必须也是二叉搜索树。
    """

    def isValidBST1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        递归实现
        """

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)

    def isValidBST2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        迭代法
        """

        if not root:
            return True

        stack = [(root, float('-inf'), float('inf')), ]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True

    def isValidBST3(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        中序遍历
        """
        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True

    # 验证是否为完全二叉树
    def isValidCBT(self, head):
        if not head:
            return True
        isLeaf = False
        queue = []
        queue.append(head)
        while queue:
            head = queue.pop(0)
            left = head.left
            right = head.right
            if (not left and right) or (isLeaf and (left or right)):
                # （not left） and  right 右边存在 左边不存在
                #  或者是进入到全是叶节点状态后 有左或者右
                # 这两种情况都会返回F
                return False
            if left:
                queue.append(left)
            if right:
                queue.append(right)
            if not left or not right:
                isLeaf = True
        return True


class Solution1:
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
