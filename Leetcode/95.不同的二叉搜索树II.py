class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def build_tree(left, right):
            all_trees = []
            if left > right:
                return [None]
            for i in range(left, right + 1):
                left_trees = build_tree(left, i - 1)
                right_trees = build_tree(i + 1, right)
                for l in left_trees:
                    for r in right_trees:
                        cur_tree = TreeNode(i)
                        cur_tree.left = l
                        cur_tree.right = r
                        all_trees.append(cur_tree)
            return all_trees

        return build_tree(1, n)