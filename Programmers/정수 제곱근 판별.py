def solution(n):
    answer = 0
    i = 1
    res = 0 # 제곱 변수
    while res < n: # 제곱 변수가 n보다 작을 때 반복
        res = i * i # 제곱해준 값 res에 대입
        if res == n: # 제곱 변수의 값이 입력값과 같다면
            i += 1 # i = i + 1
            answer = i * i # 제곱해준 값 answer에 대입
        else: # 입력값과 같지 않다면
            i += 1 # i = i + 1해서 그 다음수로 제곱
    if answer == 0: # 제곱이 아니라면
        answer = -1 # -1을 출력해주기 위해 answer에 -1 대입
    return answer

# 입출력 예시
n = 3
print(solution(n))