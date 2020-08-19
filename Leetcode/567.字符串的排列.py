class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        import collections
        s1_dic = collections.Counter(s1)

        i = 0
        j = len(s1) - 1

        while j < len(s2):
            if s1_dic == collections.Counter(s2[i:(j + 1)]):
                return True
            i += 1
            j += 1
        return False
