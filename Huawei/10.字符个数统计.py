# res = []
# for c in input():
#     if ord(c) in range(128):
#         res.append(c)
# print(len(set(res)))

print(len(set([c for c in input() if ord(c) in range(128)])))
