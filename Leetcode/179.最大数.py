class Solution(object):
    def largestNumber(self, nums):
        from functools import cmp_to_key
        def helper(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        return "".join(sorted(map(str, nums), key=cmp_to_key(helper))).lstrip("0") or "0"

    def largestNumber_magic(self, nums):
        class large_num(str):
            def __lt__(self, other):
                return self + other > other + self

        return "".join(sorted(map(str, nums), key=large_num)).lstrip("0") or "0"
