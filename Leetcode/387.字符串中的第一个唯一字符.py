class Solution(object):
    def firstUniqChar(self, s):
        dic = {}

        for c in s:
            dic[c] = dic[c] + 1 if c in dic else 1

        unique_chars = [k for k, v in filter(lambda kvp: kvp[1] == 1, dic.items())]

        for i, c in enumerate(s):
            if c in unique_chars:
                return i

        return -1

    def firstUniqChar1(self, s):
        dic = {c: s.count(c) for c in set(s)}
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1
