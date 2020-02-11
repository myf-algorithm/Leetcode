string = input().lower()
sum_str = 0
for char in string:
    num = ord(char) - ord('a') + 1
    if 0 < num <= 26:
        sum_str += num
bin_str = bin(sum_str)
x = str(bin_str).count('0') - 1
y = str(bin_str).count('1')
if y == 0:
    print(0, 0)
else:
    print(x, y)
