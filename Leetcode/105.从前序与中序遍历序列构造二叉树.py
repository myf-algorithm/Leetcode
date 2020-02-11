# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        # 前序遍历第一个值为根节点
        root = TreeNode(preorder[0])
        # 因为没有重复元素，所以可以直接根据值来查找根节点在中序遍历中的位置
        mid = inorder.index(preorder[0])
        # 构建左子树
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # 构建右子树
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root

    def buildTree_stack(self, preorder, inorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        dicts = {val: i for i, val in enumerate(inorder)}  # 构建值和其在中序遍历的位置序号对应的字典
        stack = [root]
        for i in range(1, len(preorder)):
            num = preorder[i]
            idx = dicts[num]
            interval = TreeNode(num)
            # 如果这个数的位置序号比栈中最后一个小，说明你是栈中最后一个的左子树，
            if idx < dicts[stack[-1].val]:
                stack[-1].left = interval
                stack.append(interval)
            # 比最后一个大，说明此时是某个节点的右子树
            else:
                # 出栈，使temp的val的index比idx小，idx作为temp的右子树
                while stack and idx > dicts[stack[-1].val]:  # 终止条件为栈为空，或者idx<栈顶元素序号，说明idx应该在栈顶元素的左子树中。
                    temp = stack.pop()
                temp.right = interval
                stack.append(interval)
        return root
