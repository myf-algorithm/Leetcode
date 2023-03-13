class Solution(object):
    def plusOne(self, digits):
        return list(map(int, list(str(int(''.join(map(str, digits))) + 1))))
