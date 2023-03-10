# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        cur_level = [root]  # current列表
        count = 0
        while cur_level:
            tmp = []  # 定义临时列表，存储每行的值
            next_level = []  # 定义临时列表，存储每行的节点
            for node in cur_level:
                tmp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if count & 1:
                res.append(tmp[::-1])
            else:
                res.append(tmp)
            count += 1
            cur_level = next_level
        return res

    def zigzagLevelOrder1(self, root):
        res = []

        def helper(root, depth):
            if not root:
                return
            if len(res) == depth:
                res.append([])
            if depth % 2 == 0:
                res[depth].append(root.val)
            else:
                res[depth].insert(0, root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)

        helper(root, 0)
        return res


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
    print(S.zigzagLevelOrder(root))
