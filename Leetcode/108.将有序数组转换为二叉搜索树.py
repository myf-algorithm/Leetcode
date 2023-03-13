# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        if nums is None:
            return None
        begin = 0
        end = len(nums) - 1
        return self.buildTree(nums, begin, end)

    def buildTree(self, nums, begin, end):
        if begin > end:
            return None
        mid = (begin + end) >> 1
        root = TreeNode(nums[mid])
        root.left = self.buildTree(nums, begin, mid - 1)
        root.right = self.buildTree(nums, mid + 1, end)
        return root
