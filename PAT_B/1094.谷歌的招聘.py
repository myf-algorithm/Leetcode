def main():
    L, K = (int(x) for x in input().split())
    N = input()
    answer = '404'
    if L == K:
        if is_prime(int(N)):
            answer = N
    elif L > K:
        for x in range(0, L - K + 1):
            if is_prime(int(N[x:x + K])):
                answer = N[x:x + K]
                break
    print(answer)


def is_prime(x):
    if x == 2 or x == 3 or x == 5 or x == 7:
        return True
    if x % 2 == 0 or x <= 1:
        return False
    bound = int(x ** 0.5 + 1)
    for i in range(3, bound + 1, 2):
        if x % i == 0:
            return False
    return True


if __name__ == '__main__':
    main()

