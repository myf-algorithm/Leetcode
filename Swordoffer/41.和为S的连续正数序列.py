# -*- coding:utf-8 -*-
# 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,
# 他马上就写出了正确答案是100。但是他并不满足于此,
# 他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
# 没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
# 现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

# 以计算9为例
# 1,2
# 1,2,3
# 1,2,3,4
# 2,3,4
# 2,3,4,5
# 3,4,5
# 4,5

class Solution:
    def FindContinuousSequence(self, tsum):
        small, big = 1, 2
        _len = (tsum + 1) / 2
        curr = small + big
        res = []
        while small < _len:
            if curr == tsum:
                res.append(range(small, big + 1))
            while curr > tsum and small < _len:
                curr -= small
                small += 1
                if curr == tsum:
                    res.append(range(small, big + 1))
            big += 1
            curr += big
        return res


if __name__ == "__main__":
    S = Solution()
    print(S.FindContinuousSequence(9))
