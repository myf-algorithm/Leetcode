def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


while True:
    try:
        a, b = list(map(int, input().split()))
        print(lcm(a, b))
    except:
        break
