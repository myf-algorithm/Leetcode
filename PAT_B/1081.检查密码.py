import re

p1 = re.compile("[^\wa-zA-Z.]")
str_pr = "Your password "

if __name__ == '__main__':
    n = input()
    for _ in range(int(n)):
        ps = str(input())
        if len(ps) < 6:
            print(str_pr + "is tai duan le.")
            continue
        elif p1.search(ps):
            print(str_pr + "is tai luan le.")
            continue
        elif not re.search("\d", ps):
            print(str_pr + "needs shu zi.")
            continue
        elif not re.search("[a-zA-Z]", ps):
            print(str_pr + "needs zi mu.")
            continue
        print(str_pr + "is wan mei.")
