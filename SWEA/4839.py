T = int(input()) # 테스트 케이스

def binarySearch_A(PA, l, r, c, cnt): # A에 대한 이진 탐색
    c = int((l + r) / 2) # 중간값
    if c == PA: # 중간값이 PA랑 같다면
        return cnt # 순환값 리턴
    elif c < PA: # 중간값이 A가 찾을 페이지보다 작다면
        cnt += 1 # 순환값 + 1
        l = c # 시작 페이지는 c로 바뀐다
        return binarySearch_A(PA, l, r, c, cnt)
    else: # 중간값이 A가 찾을 페이지보다 크다면
        cnt += 1 # 순환값 + 1
        r = c # 페이지 끝은 중간값으로 바뀐다
        return binarySearch_A(PA, l, r, c, cnt)

def binarySearch_B(PB, l, r, c, cnt): # B에 대한 이진 탐색
    c = int((l + r) / 2) # 중간값
    if c == PB: # 중간값이 PB랑 같다면
        return cnt # 순환값 리턴
    elif c < PB: # 중간값이 B가 찾을 페이지보다 작다면
        cnt += 1 # 순환값 + 1
        l = c # 시작 페이지는 c로 바뀐다
        return binarySearch_B(PB, l, r, c, cnt)
    else: # 중간값이 B가 찾을 페이지보다 크다면
        cnt += 1 # 순환값 + 1
        r = c # 페이지 끝은 중간값으로 바뀐다
        return binarySearch_B(PB, l, r, c, cnt)

for i in range(T):
    P, PA, PB = map(int, input().split()) # P: 페이지 끝, PA: A가 찾을 페이지, PB: B가 찾을 페이지
    l = 1 # 시작 페이지
    r = P # 페이지 끝
    c = 0 # 중간값 초기화
    cnt = 0 # 순환값 초기화
    A = binarySearch_A(PA, l, r, c, cnt) # 순환값 A에 대입
    B = binarySearch_B(PB, l, r, c, cnt) # 순환값 B에 대입

    result = "" # 결과값
    if A == B: # 순환값 A와 B가 같다면
        result = 0 # 결과값은 0이 된다
    elif A > B: # 순환값 A가 B보다 크다면
        result = "B" # B가 덜 순환해서 페이지를 찾았기 때문에 결과값 B
    else: # 순환값 A가 B보다 작다면
        result = "A" # A가 덜 순환해서 페이지를 찾았기 때문에 결과값 A

    print(f"#{i+1} {result}") # 출력