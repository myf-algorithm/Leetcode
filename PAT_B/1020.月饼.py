n, space = list(map(int, input().split()))
size = list(map(float, input().split()))
price = list(map(float, input().split()))
rate = {i: price[i] / size[i] for i in range(n)}
order = sorted(rate, key=lambda i: rate[i], reverse=True)  # 字典排序
money = 0
for i in order:
    if space >= size[i]:
        money += price[i]
        space -= size[i]
    else:
        money += space * rate[i]
        break
print('%.2f' % money)
