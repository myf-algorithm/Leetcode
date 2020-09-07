class Solution:
    def removeDuplicates(self, A):
        # write code here
        if len(A) <= 2:
            return len(A)
        dic = {}
        for i in A:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in dic.keys():
            while dic[i] > 2:
                A.remove(i)
                dic[i] -= 1
        return sum(dic.values())
