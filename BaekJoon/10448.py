from itertools import combinations_with_replacement # 중복 조합 라이브러리

T = int(input()) # 테스트 케이스
a = [int(input()) for i in range(T)] # 입력받은 수 리스트화

for i in range(len(a)):
    tri = [] # 삼각수 합 리스트
    res = 0 # 삼각수 합 변수
    result = 0 # 출력값
    for j in range(1, a[i]): # 입력받은 수의 반절 크기만큼 반복
        res += j # 삼각수의 합을 res에 대입
        tri.append(res) # 삼각수의 합을 리스트에 넣기
        if res > a[i]: # 만약 삼각수의 합이 입력받은 수와 같다면
            break # 루프 탈출
        else: # 아니라면
            continue # 반복

    N = list(combinations_with_replacement(tri, 3)) # 중복 조합으로 3개 뽑기
    for j in N:
        if sum(j) == a[i]: # 중복 조합으로 뽑은 수의 합이 입력한 수와 같다면
            result = 1
            break

    print(result)