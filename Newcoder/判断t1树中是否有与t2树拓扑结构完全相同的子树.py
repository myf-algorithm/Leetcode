# 给定彼此独立的两棵二叉树，判断 t1 树是否有与 t2 树拓扑结构完全相同的子树。
# 设 t1 树的边集为 E1，t2 树的边集为 E2，若 E2 等于 E1 ，则表示 t1 树和t2 树的拓扑结构完全相同。
# {1,2,3,4,5,6,7,#,8,9},{2,4,5,#,8,9}


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root1 TreeNode类
# @param root2 TreeNode类
# @return bool布尔型
#
a, b = input().split('},{')
a = a[1:].split(',')
b = b[:-1].split(',')
for i in range(len(a)):
    if b and a[i] == b[0]:
        b.pop(0)
    if not b:
        print('true')
        break
else:
    print('false')
