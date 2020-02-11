import sys
import re

command = ["reset", "reset board", "board add", "board delet", "reboot backplane", "backplane abort"]
op = ['reset what', 'board fault', 'where to add', 'no board at all', 'impossible', 'install first', 'unkown command']
for line in sys.stdin:
    s = line.split()
    if len(s) > 2:
        print(op[-1])
    elif len(s) == 2:
        for i in command:
            if i.find(s[1]) != -1 and i.find(s[0]) != -1:
                print(op[command.index(i)])
                break
        else:
            print(op[-1])
    elif len(s) == 1:
        for i in command:
            if i.find(s[0]) >= 0:
                print(op[command.index(i)])
                break
        else:
            print(op[-1])
