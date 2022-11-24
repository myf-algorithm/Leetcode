# 构建二叉树
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums, lo, hi):
        index, max_value = -1, float("-inf")
        # base case
        if hi < lo:
            return None

        # 找到数组中的最大值和对应的索引
        for i in range(lo, hi + 1):
            if nums[i] > max_value:
                max_value = nums[i]
                index = i

        # 构造根节点
        root = TreeNode(max_value)

        # 递归调用构造左右子树
        root.left = self.build(nums, lo, index - 1)
        root.right = self.build(nums, index + 1, hi)

        return root