class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def robTree(node):
            if not node:
                return [0, 0]  # 长度为2的数组，偷或者不偷
            left = robTree(node.left)
            right = robTree(node.right)
            val1 = node.val + left[0] + right[0]  # 偷cur_node
            val2 = max(left[0], left[1]) + max(right[0], right[1])  # 不偷cur_node
            return [val2, val1]  # 不偷当前节点得到的最大金钱，偷当前节点得到的最大金钱

        res = robTree(root)
        return max(res[0], res[1])