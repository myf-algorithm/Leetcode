a, pos, neg = input().split(), [], []
for i in a:
    neg.append(int(i)) if int(i) < 0 else pos.append(int(i))
print(len(neg))
print(round(sum(pos) / len(pos), 1) if pos else "0.0")