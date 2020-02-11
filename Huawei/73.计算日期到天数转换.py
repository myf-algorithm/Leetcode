import datetime

while True:
    try:
        print(datetime.datetime(*map(int, input().split())).strftime("%j").lstrip("0"))
    except:
        break