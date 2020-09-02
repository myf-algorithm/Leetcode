# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        时间复杂度：O(N)O\big(N\big)O(N)，NNN 是二叉树中的节点数，最坏情况下，我们需要访问二叉树的所有节点。
        空间复杂度：O(N)O(N)O(N)，这是因为递归堆栈使用的最大空间位 NNN,斜二叉树的高度可以是 NNN。
        """

        def __init__(self):
            # Variable to store LCA node.
            self.ans = None

        def recurse_tree(current_node):
            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # left Recursion
            left = recurse_tree(current_node.left)

            # right Recursion
            right = recurse_tree(current_node.right)

            # if the current node is one of p or q
            mid = current_node == p or current_node == q

            # if any two of the three flags left, right or mid become True
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans

    def lowestCommonAncestor_iter_use_parent(self, root, p, q):
        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:
            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q
