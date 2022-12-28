class Solution:
    def minDepth(self, root) -> int:
        if root is None:
            return 0
        queue = [root]
        depth = 1
        while queue:  # 遍历每层
            cur_count = len(queue)
            for i in range(cur_count):  # 遍历层内每个节点
                node = queue.pop(0)
                if (not node.left) and (not node.right):
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth