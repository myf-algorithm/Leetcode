# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        if root is None:  # 基准条件
            return []
        list += self.inorderTraversal(root.left)  # 先把左节点加入
        list.append(root.val)  # 添加根节点
        list += self.inorderTraversal(root.right)  # 添加右节点
        return list

    def inorderTraversal_iter(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res


if __name__ == '__main__':
    S = Solution()
    root = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    print(S.inorderTraversal(root))
