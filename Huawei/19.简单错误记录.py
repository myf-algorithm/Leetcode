import sys

out = []
num = {}

while True:
    input_ = sys.stdin.readline()[:-1]
    if input_ == '':
        break
    record, lines = input_.split()
    if '\\' in record:
        name = record.split('\\')[-1][-16:]
    else:
        name = record[-16:]
    item = name + ' ' + lines
    if item not in num:
        num[item] = 1
        out.append(item)
    else:
        num[item] += 1

for item in out[-8:]:
    sys.stdout.write(item + ' ' + str(num[item]) + '\n')
