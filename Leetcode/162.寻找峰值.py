class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            # ����д���� (left+right)//2 ��mid�ķ����ã�һЩ��������д���Է�ֹ���
            mid = left + (right - left) // 2
            # ������������˵��ɽ��������� mid ���Ҳ࣬��Ϊ����Ԫ�ز�ͬ������if�������� <
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


class Solution_traverse:
    def solve(self, a):
        # write code here
        n = len(a)
        if n == 1:
            return 0
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                if a[i] >= a[i - 1]:
                    return i
            elif i == 0:
                if a[i] >= a[i + 1]:
                    return i
            else:
                if a[i] >= a[i - 1] and a[i] >= a[i + 1]:
                    return i
        return -1


class Solution_traverse_a:
    def solve(self, a):
        a.insert(0, float('-inf'))
        a.append(float('-inf'))
        res = []
        for i in range(1, len(a) - 1):
            if a[i] >= a[i - 1] and a[i] >= a[i + 1]:
                res.append(i - 1)
        return max(res)
