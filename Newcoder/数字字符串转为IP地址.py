# @param s string×Ö·û´®
# @return string×Ö·û´®Ò»Î¬Êý×é

class Solution:
    def restoreIpAddresses(self, s):
        # write code here
        self.res = []

        def backtrack(curr, rest):
            if len(curr) == 4:
                if len(rest) > 0:
                    return
                self.res.append(".".join(curr))
            else:
                if not rest:
                    return
                for i in range(1, 4):
                    if rest[0] == "0" and i > 1:
                        continue
                    if i <= len(rest) and int(rest[:i]) <= 255:
                        curr.append(rest[:i])
                        backtrack(curr, rest[i:])
                        curr.pop()

        backtrack([], s)
        return self.res
