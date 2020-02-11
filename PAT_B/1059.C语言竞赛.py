N = int(input())
rank = {}
for i in range(N):
    name = input()
    rank[name] = i + 1


def isprime(num):
    if num != 2 and num % 2 == 0:
        return False
    import math
    flag = True
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            flag = False
            break
    return flag


K = int(input())
for i in range(K):
    query = input()
    if query in rank.keys():
        ranking = rank[query]
        if ranking == 1:
            msg = "Mystery Award"
        elif ranking == -1:
            msg = "Checked"
        elif isprime(ranking):
            msg = "Minion"
        else:
            msg = "Chocolate"
        rank[query] = -1
    else:
        msg = "Are you kidding?"
    print("%04s: %s" % (query, msg))
