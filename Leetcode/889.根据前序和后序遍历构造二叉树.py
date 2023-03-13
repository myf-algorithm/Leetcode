# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build_tree(preorder, postorder):
            if not preorder:
                return None

            # 数组长度为1时，直接返回即可
            if len(preorder) == 1:
                return TreeNode(preorder[0])

            # 根据前序数组的第一个元素，创建根节点
            root = TreeNode(preorder[0])

            # 根据前序数组第二个元素，确定后序数组左子树范围
            index = postorder.index(preorder[1]) + 1

            # 递归构造左右子树
            root.left = build_tree(preorder[1:index + 1], postorder[:index])
            root.right = build_tree(preorder[index + 1:], postorder[index:-1])
            return root

        return build_tree(preorder, postorder)
