import sys

while True:
    n = sys.stdin.readline().strip()
    if n:
        n = int(n)
        while n > 0:
            n = n - 1
            s = sys.stdin.readline().strip()
            if len(s) % 8 > 0:
                s = s + (8 - len(s) % 8) * '0'
            st = ''
            for i in range(len(s)):
                st = st + s[i]
                if (i + 1) % 8 == 0:
                    print(st)
                    st = ''
    else:
        break