# -*- coding:utf-8 -*-
# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
# 打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
# 则打印出这三个数字能排成的最小数字为321323。

# 比较两个字符串s1, s2大小的时候，先将它们拼接起来，比较s1+s2,和s2+s1那个大
# 如果s1+s2大，那说明s2应该放前面，所以按这个规则，s2就应该排在s1前面

# list.sort()：list会发生改变，只能在列表上使用
# new_list = sorted(list)：list不会发生改变，返回结果给new_list，可在列表、字典上使用
# sort和sorted的key参数：指定一个函数，此函数只有一个参数，返回一个值进行比较
# 在python3中，提供将cmp转化为key的函数
# cmp参数指定的函数需要2个参数，用来进行元素间的比较
# 返回负数表示小于
# 0表示等于
# 正数表示大于


class Solution:
    def PrintMinNumber(self, numbers):
        from functools import cmp_to_key
        if not numbers:
            return ""
        # 输入字符串转化为列表，列表中存储各位数字的字符
        numbers = list(map(str, numbers))
        # 使用cmp_to_key和lambda方法进行排序
        numbers.sort(key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)))
        return '0' if numbers[0] == '0' else ''.join(numbers)


if __name__ == '__main__':
    S = Solution()
    print(S.PrintMinNumber([3, 32, 321]))

    # sorted中key参数的使用方法
    student1 = {
        "age": 152
    }
    student2 = {
        "age": 132
    }
    student3 = {
        "age": 122
    }
    student4 = {
        "age": 1223
    }
    student_list = [student1, student2, student3, student4]
    print(sorted(student_list, key=lambda student: student["age"]))
