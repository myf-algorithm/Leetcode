# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth_bfs(self, root):
        if root is None:
            return 0
        queue = [(1, root)]
        depth = 0
        while queue:
            depth, node = queue.pop(0)
            if node.left:
                queue.append((depth + 1, node.left))
            if node.right:
                queue.append((depth + 1, node.right))
        return depth

    def maxDepth_dfs(self, root):
        if root is None:
            return 0

        stack = [(1, root)]
        depth = 0
        while stack:
            cur_dep, node = stack.pop()
            depth = max(depth, cur_dep)
            if node.right:
                stack.append((cur_dep + 1, node.right))
            if node.left:
                stack.append((cur_dep + 1, node.left))
        return depth

    def maxDepth_dfs_r(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth_dfs_r(root.left)
            right_height = self.maxDepth_dfs_r(root.right)
            return max(left_height, right_height) + 1


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
    print(S.maxDepth_bfs(root))
