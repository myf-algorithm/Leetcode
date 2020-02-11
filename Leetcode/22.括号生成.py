from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        pre = set({'()', })
        for i in range(n - 1):
            now = set()
            for st in pre:
                n = len(st)
                for index in range(n):
                    now.add(st[0:index] + '()' + st[index:n])
            pre = now
        return list(pre)

    def generateParenthesis_backTrack(self, n: int) -> List[str]:
        """
        时间复杂度：O(4^n/n^0.5)
        空间复杂度：O(4^n/n^0.5)
        """
        ans = []

        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)

        backtrack()
        return ans


    def generateParenthesis_dp(self, n: int) -> List[str]:
        """
        考虑 i=n 时相比 n-1 组括号增加的那一组括号的位置

        """
        if n == 0:
            return []
        total_l = []
        total_l.append(None)  # 0组括号记为None
        total_l.append("()")  # 1组括号只有一种情况
        for i in range(2, n + 1):  # 开始
            l = []
            for j in range(i):  # 开始遍历p, q, 其中p + q = i - 1, j作为索引
                now_list1 = total_l[j]  # p = j 时括号组合情况
                now_list2 = total_l[i - 1 - j]  # q = (i - 1) - j 时的括号组合情况
                for k1 in now_list1:
                    for k2 in now_list2:
                        if k1 == None:
                            k1 = ""
                        if k2 == None:
                            k2 = ""
                        el = "(" + k1 + ")" + k2
                        l.append(el)  # 把所有可能的情况添加到l中
            total_l.append(l)  # l这个list就是i组括号的所有情况，添加到total_l中，继续求解i=i+1的情况
        return total_l[n]


if __name__ == '__main__':
    S = Solution()
    print(S.generateParenthesis_backTrack(3))
