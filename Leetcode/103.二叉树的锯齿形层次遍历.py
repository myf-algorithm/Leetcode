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
        cur_level = [root]
        count = 0
        while cur_level:
            tmp = []
            next_level = []
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

    def zigzagLevelOrder2(self, root):
        """
        双栈实现
        """
        if not root:
            return []

        d1 = []  # 从左向右存储的栈
        d2 = []  # 从右向左存储的栈 d2和d1完成锯齿状存储的任务
        res = []  # 保存输出结果
        tmp = []  # 临时存储结果
        d1.append(root)
        while (True):
            while d1:
                curr = d1[-1]
                d1.pop()
                tmp.append(curr.val)
                if curr.left:  # 左边的节点先入栈
                    d2.append(curr.left)
                if curr.right:
                    d2.append(curr.right)
            if tmp:
                res.append(tmp)
                tmp = []
            else:
                break

            while d2:
                curr = d2[-1]
                d2.pop()
                tmp.append(curr.val)
                if curr.right:  # 这里是右边的节点先入栈
                    d1.append(curr.right)
                if curr.left:
                    d1.append(curr.left)
            if tmp:
                res.append(tmp)
                tmp = []
            else:
                break
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
