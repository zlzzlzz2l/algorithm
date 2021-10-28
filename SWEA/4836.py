T = int(input()) # 테스트 케이스

for test in range(T): # 테스트 케이스만큼 반복
    N = int(input()) # 영역 개수
    cnt = 0 # 겹친 영역 개수
    a = [] # 영역 범위
    b = [] # 빨강 영역 범위
    c = [] # 파랑 영역 범위
    for i in range(N): # 영역 개수만큼 반복
        a.append(list(map(int, input().split()))) # 영역 범위 입력받기

    for i in range(len(a)): # 영역 범위만큼 반복
        for t in range(a[i][0], a[i][2]+1): # r1, r2
            for j in range(a[i][1], a[i][3]+1): # c1, c2
                if a[i][-1] == 1: # 빨강 영역일 때
                    b.append([t, j])
                else: # 파란 영역 일 때
                    c.append([t, j])

    for s in range(0, len(b)): # 순차검색 이용
        for j in range(0, len(c)):
            if b[s] == c[j]:
                cnt += 1 # b와 c에 같은 범위가 있다면 겹친 영역 개수 +1
    print(f"#{test+1} {cnt}")