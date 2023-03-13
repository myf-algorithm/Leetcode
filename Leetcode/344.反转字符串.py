class Solution(object):
    def reverseString_rec(self, s):
        def recur(tmps):
            if len(tmps) <= 1:
                return tmps
            else:
                return recur(tmps[1:]) + [tmps[0]]

        s[:] = recur(s)

    def reverseString_double_point(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    def reverseString_rec_double_point(self, s):
        def recur_(s, i, j):
            if i >= j:
                return
            else:
                s[i], s[j] = s[j], s[i]
                recur_(s, i + 1, j - 1)

        recur_(s, 0, len(s) - 1)
