# �����˴˶��������ö��������ж� t1 ���Ƿ����� t2 �����˽ṹ��ȫ��ͬ��������
# �� t1 ���ı߼�Ϊ E1��t2 ���ı߼�Ϊ E2���� E2 ���� E1 �����ʾ t1 ����t2 �������˽ṹ��ȫ��ͬ��
# {1,2,3,4,5,6,7,#,8,9},{2,4,5,#,8,9}


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root1 TreeNode��
# @param root2 TreeNode��
# @return bool������
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
