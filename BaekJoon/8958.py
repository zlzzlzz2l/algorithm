import sys
N = int(input()) # 테스트 케이스 입력

for i in range(N): # 테스트 케이스만큼 반복
    OX = sys.stdin.readline().strip() # OX 문자열 입력
    cnt = 0 # 카운트 0으로 초기화
    o = 0 # o일 때 반복 0으로 초기화
    for j in OX: # OX 문자열만큼 반복
        if j == "X": # X일 때
            o = 0 # o은 0으로 대입
        else: # O일 때
            o += 1 # o은 +1
            cnt += o # 카운트도 o만큼 더하기
    print(cnt)