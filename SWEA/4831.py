def straight(a, c, N, K, b):
    while True:
        a += K # 현재위치에다가 최대이동수 더하기
        if a >= N: # 현재위치가 도착지보다 크면
            break
        for i in range(a, a-K, -1): # 현재위치+K에서 현재위치-K까지 -1만큼 반복
            if c[i] == 0: # 충전기가 설치된 곳이면
                a = i # 현재위치는 i
                b += 1 # 움직인 횟수 1 더하기
                break
        else: # 현재위치가 도착지보다 작으면
            b = 0 # 도착지까지 못가니까 0이 된다.
            break
    return b

T = int(input()) # 테스트 케이스

for d in range(T):
    K, N, M = map(int, input().split()) # K: 최대이동, N: 도착지, M: 충전기 개수
    num = list(map(int, input().split())) # 충전기 설치된 곳

    c = [1] * (N+1) # 충전기 설치된 곳 리스트 초기화

    # 충전기 설치된 곳은 0으로 바꾸기
    for i in range(N):
        for j in range(len(num)):
            if num[j] == i:
                c[i] = 0
            else:
                continue

    global a # 현재 위치
    global b # 움직인 횟수
    a = 0
    b = 0
    result = straight(a, c, N, K, b)
    print(f"#{d+1} {result}")
