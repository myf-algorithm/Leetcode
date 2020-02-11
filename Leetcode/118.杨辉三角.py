class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        tmp = []
        for _ in range(numRows):
            tmp.insert(0, 1)
            for i in range(1, len(tmp) - 1):
                tmp[i] = tmp[i] + tmp[i + 1]
            res.append(tmp[:])
        return res

    def generate_l(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l = []
        for n in range(numRows):
            if n < 2:
                n_row = [1 for i in range(n + 1)]
            else:
                last_row = l[-1]
                row_mid = [last_row[i] + last_row[i + 1] for i in range(n - 1)]
                n_row = [1] + row_mid + [1]
            l.append(n_row)
        return l

    def generate_dp(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        numRows -= 2
        rList = [[1], [1, 1]]
        while numRows > 0:
            newlist = [1]
            for i in range(len(rList[-1]) - 1):
                newlist.append(rList[-1][i] + rList[-1][i + 1])
            newlist.append(1)
            rList.append(newlist)
            numRows -= 1
        return rList


if __name__ == '__main__':
    S = Solution()
    print(S.generate(5))
