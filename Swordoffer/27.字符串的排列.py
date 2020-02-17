# -*- coding:utf-8 -*-
# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
# 例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串
# abc,acb,bac,bca,cab和cba。


class Solution:
    # 返回 RandomListNode
    def Permutation(self, ss):
        def dfs(s):
            if len(s) == '':
                return []
            if len(s) == 1:
                return [s]
            if len(s) == 2:
                return list(set([s[0] + s[1], s[1] + s[0]]))
            ans = set([])
            left = s[0]  # 数组的首元素
            right = dfs(s[1:])  # 数组的剩余元素
            for word in right:
                for i in range(len(word) + 1):
                    ans.add(word[:i] + left + word[i:])
            return list(ans)

        if ss == '':
            return []
        return sorted(dfs(ss))


class Solution1:
    def Permutation(self, ss):
        list = []
        if len(ss) <= 1:
            return ss
        for i in range(len(ss)):
            # 生成每个排好序的字符串（lambda补全每个循环中返回字符串的头部）
            for j in map(lambda x: ss[i] + x, self.Permutation(ss[:i] + ss[i + 1:])):
                # 这里的判断可以消除重复值的影响
                if j not in list:
                    list.append(j)
        return list


class Solution2:
    def Permutation(self, ss):
        if not ss:
            return []
        res = []
        self.helper(ss, res, '')
        return sorted(list(set(res)))

    def helper(self, ss, res, path):
        if not ss:
            res.append(path)
        else:
            for i in range(len(ss)):
                self.helper(ss[:i] + ss[i + 1:], res, path + ss[i])


if __name__ == '__main__':
    S = Solution1()
    print(S.Permutation("abc"))
