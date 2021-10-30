from itertools import combinations # 조합 라이브러리

T = int(input()) # 테스트 케이스

A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12} # 1-12까지 수를 가지고 있는 집합 A
cnt = 0 # 가짓수

for i in range(T): # 테스트 케이스만큼 반복
    N, K = map(int, input().split()) # N: 뽑을 개수, K: 원소의 합
    col = list(combinations(A, N)) # A 집합에서 N개 뽑기
    for j in col: # N개 뽑은 수만큼 반복
        if sum(j) == K: # 뽑은 수가 입력값 원소의 합과 같다면
            cnt += 1 # 가짓수 +1
    print(f"#{i+1} {cnt}")
    cnt = 0 # 가짓수 초기화