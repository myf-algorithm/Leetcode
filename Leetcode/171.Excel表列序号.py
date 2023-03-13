class Solution(object):
    def titleToNumber(self, s):
        if not s:
            return 0
        res = 0
        tmp = 1
        for i in s[::-1]:
            res += (int(ord(i) - ord('A')) + 1) * tmp
            tmp *= 26
        return res

    def titleToNumber_1(self, s):
        return sum((ord(a) - 64) * (26 ** i) for i, a in enumerate(s[::-1]))
