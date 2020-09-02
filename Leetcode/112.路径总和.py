# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution_DFS:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


class Solution_Back(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        res = []
        return self.dfs(root, sum, res, [root.val])

    def dfs(self, root, target, res, path):
        if not root: return False
        if sum(path) == target and not root.left and not root.right:
            return True
        left_flag, right_flag = False, False
        if root.left:
            left_flag = self.dfs(root.left, target, res, path + [root.left.val])
        if root.right:
            right_flag = self.dfs(root.right, target, res, path + [root.right.val])
        return left_flag or right_flag


import collections


class Solution:
    def hasPathSum_BFS(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        que = collections.deque()
        que.append((root, root.val))
        while que:
            node, path = que.popleft()
            if not node.left and not node.right and path == sum:
                return True
            if node.left:
                que.append((node.left, path + node.left.val))
            if node.right:
                que.append((node.right, path + node.right.val))
        return False


class Solution_Stack(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = []
        stack.append((root, root.val))
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right and path == sum:
                return True
            if node.left:
                stack.append((node.left, path + node.left.val))
            if node.right:
                stack.append((node.right, path + node.right.val))
        return False
