DNA = input()
length = int(input())
top, index = 0, 0
for i in range(len(DNA) + 1 - length):
    sub = DNA[i:i + length]
    GC_Ratio = (sub.count('G') + sub.count('C')) / len(sub)
    if GC_Ratio > top:
        top = GC_Ratio
        index = i
print(DNA[index:index + length])
