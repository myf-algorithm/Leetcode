class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build_tree(postorder, inorder):
            if len(postorder) == 0:
                return None

            root_val = postorder[-1]
            root = TreeNode(root_val)

            index = inorder.index(root_val)
            inorder_left = inorder[:index]
            inorder_right = inorder[index + 1:]
            postorder_left = postorder[:index]
            postorder_right = postorder[index:-1]

            root.left = build_tree(postorder_left, inorder_left)
            root.right = build_tree(postorder_right, inorder_right)
            return root
        return build_tree(postorder, inorder)