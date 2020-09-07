class Solution1:
    def permuteUnique(self, num):
        # write code here
        num.sort()
        res = []
        auxiliary = []
        findOut = [0 for i in range(len(num))]

        def backtrack(num, res, auxiliary):
            if len(auxiliary) == len(num):
                res.append(auxiliary[:])
                return
            for i in range(len(num)):
                if i >= 1 and num[i - 1] == num[i]:
                    if findOut[i - 1] == 0:
                        continue
                if findOut[i] == 1:
                    continue
                auxiliary.append(num[i])
                findOut[i] = 1
                backtrack(num, res, auxiliary)
                auxiliary.pop()
                findOut[i] = 0

        backtrack(num, res, auxiliary)
        return res


class Solution2:
    def permuteUnique(self, num):
        # write code here
        def helper(num, s, e, ret):
            if s == e:
                return
            elif s == e - 1:
                t = list(num)
                if t not in ret:
                    ret.append(t)
            else:
                for i in range(s, e):
                    num[i], num[s] = num[s], num[i]
                    helper(num, s + 1, e, ret)
                    num[i], num[s] = num[s], num[i]

        ret = []
        helper(num, 0, len(num), ret)
        return sorted(ret)
