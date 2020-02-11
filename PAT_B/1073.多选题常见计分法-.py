def get_input(M, dir_right_answers, list_grades):
    # 得到所有标准答案并存放在字典中, 并返回分数list
    for i in range(M):
        string_right = input()
        dir_right_answers[i] = string_right
        list_grades.append(int(string_right[0]))


def deal_my_answer(string_my_answer):
    # 对学生的答案进行处理，得到标准的list
    string_my_answer = string_my_answer[1:-1]
    string_my_answer = string_my_answer.split(') (')
    return string_my_answer


def judge_wrong_or_partRight(my_answer, right_answer):
    # 一个同学的某个答案在没有全对的情况下判断是属于全错还是部分对的情况
    wrong_flag = False
    for num in my_answer:
        if num not in right_answer:
            wrong_flag = True
    return wrong_flag


def get_part_right_per_count(right_answer, my_answer, list_wrong, count_per):
    # 得到部分正确选项的遗漏选项次数
    for num in right_answer:
        if num not in my_answer:
            if num not in list_wrong:
                list_wrong.append(num)  # 从来没有的加入到错误选项list
                count_per[num] = 1
            else:
                count_per[num] += 1


def get_wrong_count(right_answer, my_answer, list_wrong, count_per):
    # 得到错误答案选项中的次数
    right_answer_copy = right_answer
    for num in my_answer:
        if num in right_answer:
            right_answer_copy.remove(num)
        elif num not in list_wrong:
            list_wrong.append(num)
            count_per[num] = 1
        else:
            count_per[num] += 1
    if right_answer_copy:
        for num in right_answer_copy:
            if num not in list_wrong:
                list_wrong.append(num)  # 从来没有的加入到错误选项list
                count_per[num] = 1
            else:
                count_per[num] += 1


def judge_my_answer(M, string_my_answer, dir_right_answers, list_grades, dir_count_wrong, dir_list_wrong,
                    flag_wrong):
    # 判断一个同学的答案是否正确, 并且得到其本道题的分数
    my_grades = 0
    for i in range(M):
        wrong_flag = False
        right_answer = dir_right_answers[i].split()
        right_answer = right_answer[3:]  # 得到只含选项的正确答案
        my_answer = string_my_answer[i].split()
        my_answer = my_answer[1:]  # 得到只含选项的同学所做答案
        if my_answer == right_answer:
            my_grades += list_grades[i]  # 全对的情况
        else:  # 其他的情况
            flag_wrong = True
            wrong_flag = judge_wrong_or_partRight(my_answer, right_answer)
            if wrong_flag:
                get_wrong_count(right_answer, my_answer, dir_list_wrong[i], dir_count_wrong[i])
            else:
                my_grades += list_grades[i] * 0.5
                get_part_right_per_count(right_answer, my_answer, dir_list_wrong[i], dir_count_wrong[i])
    print("%.1f" % my_grades)
    return flag_wrong


def get_initilazition_list(M, dir_list_wrong, dir_count_wrong):
    # 初始化存放错误选项的list以及存放错误次数的字典
    for i in range(M):
        dir_list_wrong[i] = []
        dir_count_wrong[i] = {}


def get_max_count(M, dir_count_wrong, dir_list_wrong):
    # 寻找错误次数最多的选项
    dir_max = {}
    list_count_all = []
    for i in range(M):
        list_count = []
        my_dir = dir_count_wrong[i]
        for num in dir_list_wrong[i]:
            list_count.append(my_dir[num])
        dir_max[i] = max(list_count)
        list_count_all.append(dir_max[i])
    max_all = max(list_count_all)

    # 列出所有的错误次数最多的选项
    for i in range(M):
        if dir_max[i] == max_all:
            my_wrong_list = dir_list_wrong[i]
            my_wrong_list = sorted(my_wrong_list)
            for num in my_wrong_list:
                if dir_count_wrong[i][num] == max_all:
                    print("%d %d-%s" % (max_all, i + 1, num))


if __name__ == '__main__':
    string_N_AND_M = input().split()
    N, M = int(string_N_AND_M[0]), int(string_N_AND_M[1])
    dir_right_answers = {}  # 存放正确答案的字典
    flag_wrong = False  # 标识是否有错误答案
    dir_count_wrong = {}  # 存放每个题所有错误答案次数的字典
    dir_list_wrong = {}  # 存放每一题错误选项list的字典
    get_initilazition_list(M, dir_list_wrong, dir_count_wrong)
    list_grades = []  # 存放每个题分数的list
    get_input(M, dir_right_answers, list_grades)
    for i in range(N):  # 对每一个同学的情况进行分析
        string_my_answer = input()
        string_my_answer = deal_my_answer(string_my_answer)
        flag_wrong = judge_my_answer(M, string_my_answer, dir_right_answers, list_grades,
                                     dir_count_wrong, dir_list_wrong, flag_wrong)
    if flag_wrong:
        get_max_count(M, dir_count_wrong, dir_list_wrong)
    else:
        print("Too simple")
