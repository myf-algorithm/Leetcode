class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def widthOfBinaryTree(self, root):
        queue = [(root, 0, 0)]  # node, depth, pos
        cur_depth = 0
        left = 0
        ans = 0
        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth + 1, pos * 2))
                queue.append((node.left, depth + 1, pos * 2 + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                ans = max(pos - left + 1, ans)
        return ans


if __name__ == "__main__":
    S = Solution()
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(1)
    node4 = TreeNode(2)
    root.left = node1
    root.right = node2
    node1.left = node3
    node2.left = node4
    print(S.IsBalanced_Solution(root))
