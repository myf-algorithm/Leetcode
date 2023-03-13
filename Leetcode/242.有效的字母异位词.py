class Solution(object):
    def isAnagram(self, s, t):
        s = [i for i in s]
        t = [i for i in t]
        s.sort()
        t.sort()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True

    def isAnagram1(self, s, t):
        import collections
        return collections.Counter(s) == collections.Counter(t)

    def isAnagram_hash(self, s, t):
        dic = {}

        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        for i in t:
            if i not in dic or dic[i] <= 0:
                return False
            dic[i] -= 1

        for i in dic:
            if dic[i] != 0:
                return False
        return True