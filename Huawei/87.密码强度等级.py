while True:
    try:
        password = input()
        grade = 0
        # 一、密码长度:
        def grade_length(s):
            length = len(s)
            grade = 0
            if length <= 4:
                grade += 5
            elif 5 <= length <= 7:
                grade += 10
            else:
                grade += 25
            return grade


        # 二、字母:三、数字:
        def grade_char(s):
            check_char = [False, False, False, False, False, False]  # 小写，大写，数字，大于1个数字，符号，大于1个符号
            nums_digit, nums_symbol = 0, 0
            grade = 0
            for i in set(s):
                if 'a' <= i <= 'z':
                    check_char[0] = True
                elif 'A' <= i <= "Z":
                    check_char[1] = True
                elif '0' <= i <= "9":
                    check_char[2] = True
                    nums_digit += 1
                else:
                    check_char[4] = True
                    nums_symbol += 1
            if nums_digit > 1:
                check_char[3] = True
                grade += 5  # 最后统一每个+10分
            if nums_symbol > 1:
                check_char[5] = True
                grade += 5
            grade += check_char.count(True) * 10
            # 奖励
            if check_char[0] and check_char[1] and check_char[2] and check_char[4]:
                grade += 5
            elif (check_char[0] or check_char[1]) and check_char[2] and check_char[4]:
                grade += 3
            elif (check_char[0] or check_char[1]) and check_char[2]:
                grade += 2
            return grade

        grade = grade_length(password) + grade_char(password)

        if grade >= 90:
            print('VERY_SECURE')
        elif grade >= 80:
            print('SECURE')
        elif grade >= 70:
            print('VERY_STRONG')
        elif grade >= 60:
            print('STRONG')
        elif grade >= 50:
            print('AVERAGE')
        elif grade >= 25:
            print('WEAK')
        else:
            print('VERY_WEAK')
    except:
        break