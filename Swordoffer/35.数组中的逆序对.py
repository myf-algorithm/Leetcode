# -*- coding:utf-8 -*-
# 在数组中的两个数字，如果前面一个数字大于后面的数字，
# 则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
# 并将P对1000000007取模的结果输出。 即输出P%1000000007

# 题目保证输入的数组中没有的相同的数字，数据范围：
# 对于%50的数据,size<=10^4
# 对于%75的数据,size<=10^5
# 对于%100的数据,size<=2*10^5

class Solution:
    def InversePairs(self, data):
        length = len(data)
        if data == None or length <= 0:
            return 0
        copy = [0] * length
        for i in range(length):
            copy[i] = data[i]
        count = self.InversePairsCore(data, copy, 0, length - 1)
        return count

    def InversePairsCore(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        length = (end - start) // 2
        left = self.InversePairsCore(copy, data, start, start + length)
        right = self.InversePairsCore(copy, data, start + length + 1, end)
        i = start + length  # i初始化为前半段最后一个数字的下标
        j = end  # j初始化为后半段最后一个数字的下标
        indexCopy = end
        count = 0

        while i >= start and j >= start + length + 1:
            if data[i] > data[j]:
                copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j - start - length
            else:
                copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1

        while i >= start:
            copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1

        while j >= start + length + 1:
            copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1
        return left + right + count

    def quick_sort(self, data):
        if len(data) < 2:
            return data
        left = self.quick_sort([i for i in data[1:] if i <= data[0]])
        right = self.quick_sort([j for j in data[1:] if j > data[0]])
        return left + [data[0]] + right

    def InversePairs1(self, data):
        count = 0
        copy = []
        for i in data:
            copy.append(i)
        copy = self.quick_sort(copy)
        for i in range(len(copy)):
            count += data.index(copy[i])
            data.remove(copy[i])
        return count % 1000000007


count = 0


class Solution1:
    def InversePairs(self, data):
        global count
        def MergeSort(lists):
            global count
            if len(lists) <= 1:
                return lists
            num = int(len(lists) / 2)
            left = MergeSort(lists[:num])
            right = MergeSort(lists[num:])
            r, l = 0, 0
            result = []
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
                    count += len(left) - l
            result += right[r:]
            result += left[l:]
            return result
        MergeSort(data)
        return count % 1000000007


if __name__ == '__main__':
    S = Solution1()
    print(S.InversePairs([1, 2, 3, 4, 5, 6, 7, 0]))
