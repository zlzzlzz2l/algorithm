def straight(a, c, N, K, b):
    for i in range(a, N, K):
        if c[i] == 0:
            if a >= (N - a):
                b += 1
                break
            b += 1
            a = i
            continue
        elif c[i] == 1:
            if a >= (N - a):
                b += 1
                break
            for j in range(i - 1, i-K, -1):
                if c[j] == 0:
                    a = j
                    b += 1
                    return straight(a + K, c, N, K, b)
                elif c[j] == 1:
                    continue
            return 0
    return b


T = int(input()) # 테스트 케이스

for d in range(T):
    K, N, M = map(int, input().split())
    num = list(map(int, input().split()))

    c = [1] * (N+1)

    for i in range(N):
        for j in range(len(num)):
            if num[j] == i:
                c[i] = 0
            else:
                continue

    global a # 현재 위치
    global b # 움직인 횟수
    a = K
    b = 0
    result = straight(a, c, N, K, b)
    print(f"#{d+1} {result}")
