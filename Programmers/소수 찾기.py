def solution(n):
    answer = 0
    for i in range(2, n+1): # 입력값들 내에서 소수 찾기
        cnt = 0
        for j in range(2, i): # 2부터 자기 자신까지 반복
            if i % j == 0:
                cnt += 1
                break
        if cnt == 0:
            answer += 1

    return answer

# 입출력 예시
n = 10
print(solution(n))