# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        递归实现
        """
        if not root:
            return True

        def match(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            return l.val == r.val and match(l.left, r.right) and match(l.right, r.left)

        return match(root.left, root.right)

    def isSymmetric1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        迭代实现
        """
        from collections import deque
        deq = deque([root, root])

        while deq:
            t1, t2 = deq.pop(), deq.pop()
            # 两个节点都为空, 则继续判断
            if not t1 and not t2:
                continue
            # 存在一个节点为空, 则为False
            if not (t1 and t2):
                return False
            if t1.val != t2.val:
                return False
            # t1, t2的左右节点, 要对称的写入双端队列中
            deq.append(t1.left)
            deq.append(t2.right)
            deq.append(t1.right)
            deq.append(t2.left)
        return True


if __name__ == '__main__':
    S = Solution()
    root = TreeNode(5)
    node1 = TreeNode(3)
    node2 = TreeNode(3)
    root.left = node1
    root.right = node2
    print(S.isSymmetric(root))
