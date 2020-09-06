class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals)
        res = []
        n = len(intervals)
        i = 0
        while i < n:
            left = intervals[i][0]
            right = intervals[i][1]
            # ��һ����ߵ�ֵС�ڵ��ڵ�ǰ�ұߵ�ֵ���ϲ�
            while i < n - 1 and intervals[i + 1][0] <= right:
                i += 1
                # ���������ұߵ�ֵ
                right = max(intervals[i][1], right)
            res.append([left, right])
            i += 1
        return res


if __name__ == '__main__':
    S = Solution()
    a = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(S.merge(a))
