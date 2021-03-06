class Solution(object):
    def countAndSay(self, n):
        prev_person = '1'
        for i in range(1, n):
            next_person, num, count = '', prev_person[0], 1
            for j in range(1, len(prev_person)):
                if prev_person[j] == num:
                    count += 1
                else:
                    next_person += str(count) + num
                    num = prev_person[j]
                    count = 1
            next_person += str(count) + num
            prev_person = next_person
        return prev_person


if __name__ == '__main__':
    S = Solution()
    print(S.countAndSay(4))
