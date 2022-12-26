class Solution:
    def strStr_naive(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

    def strStr_sunday(self, haystack: str, needle: str) -> int:
        # 计算偏移表
        def calShiftMat(st):
            dic = {}
            for i in range(len(st) - 1, -1, -1):
                if not dic.get(st[i]):
                    dic[st[i]] = len(st) - i
            dic["ot"] = len(st) + 1
            return dic

        # 其他情况判断
        if len(needle) > len(haystack):
            return -1
        if needle == "":
            return 0

        # 偏移表预处理
        dic = calShiftMat(needle)
        idx = 0

        while idx + len(needle) <= len(haystack):
            # 待匹配字符串
            str_cut = haystack[idx:idx + len(needle)]

            # 判断是否匹配
            if str_cut == needle:
                return idx
            else:
                # 边界处理
                if idx + len(needle) >= len(haystack):
                    return -1

                # 不匹配情况下，根据下一个字符的偏移，移动idx
                cur_c = haystack[idx + len(needle)]
                if dic.get(cur_c):
                    idx += dic[cur_c]
                else:
                    idx += dic["ot"]

        return -1 if idx + len(needle) >= len(haystack) else idx

    def strStr_kmp(self, haystack: str, needle: str) -> int:
        # KMP 匹配算法，T 为文本串，p 为模式串
        def kmp(T: str, p: str) -> int:
            n, m = len(T), len(p)

            next = generateNext(p)  # 生成 next 数组

            i, j = 0, 0
            while i < n and j < m:
                if j == -1 or T[i] == p[j]:
                    i += 1
                    j += 1
                else:
                    j = next[j]
            if j == m:
                return i - j

            return -1

        # 生成 next 数组
        # next[i] 表示坏字符在模式串中最后一次出现的位置
        def generateNext(p: str):
            m = len(p)

            next = [-1 for _ in range(m)]  # 初始化数组元素全部为 -1
            i, k = 0, -1
            while i < m - 1:  # 生成下一个 next 元素
                if k == -1 or p[i] == p[k]:
                    i += 1
                    k += 1
                    if p[i] == p[k]:
                        next[i] = next[k]  # 设置 next 元素
                    else:
                        next[i] = k  # 退到更短相同前缀
                else:
                    k = next[k]
            return next

        return kmp(haystack, needle)


if __name__ == '__main__':
    s = Solution()
    print(s.strStr_naive(haystack="aaa", needle="a"))
