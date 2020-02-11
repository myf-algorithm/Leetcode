import sys

while True:
    input = sys.stdin.readline().strip()
    if input == "":
        break
    res = ""
    for c in input:
        if 'A' <= c and c <= 'Y':
            c = chr(ord(c) + 1).lower()
        elif c == 'Z':
            c = 'a'
        elif 'a' <= c and c <= 'c':
            c = '2'
        elif 'd' <= c and c <= 'f':
            c = '3'
        elif 'g' <= c and c <= 'i':
            c = '4'
        elif 'j' <= c and c <= 'l':
            c = '5'
        elif 'm' <= c and c <= 'o':
            c = '6'
        elif 'p' <= c and c <= 's':
            c = '7'
        elif 't' <= c and c <= 'v':
            c = '8'
        elif 'w' <= c and c <= 'z':
            c = '9'
        else:
            c = c
        res += c
    print(res)