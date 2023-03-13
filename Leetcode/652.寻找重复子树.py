# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict


class Solution:
    def __init__(self):
        self.res = []
        self.hashmap = {}

    def traverse(self, root):
        if root is None:
            return '#'
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        subtree = left + ',' + right + ',' + str(root.val)

        count = self.hashmap.get(subtree, 0)
        if count == 1:
            self.res.append(root)
        self.hashmap[subtree] = count + 1

        return subtree

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.traverse(root)
        return self.res
