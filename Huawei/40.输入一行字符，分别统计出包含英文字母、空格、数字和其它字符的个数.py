while True:
    try:
        a = input()
        char, space, number, other = 0, 0, 0, 0
        for i in a:
            if i == " ":
                space += 1
            elif i.isnumeric():
                number += 1
            elif i.isalpha():
                char += 1
            else:
                other += 1
        print(char)
        print(space)
        print(number)
        print(other)
    except:
        break
