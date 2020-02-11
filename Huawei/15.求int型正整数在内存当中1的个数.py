n = int(input())
print(bin(n).replace("0b", "").count("1"))
