def solution(num):
    answer = 0
    while num != 1: # 입력값이 1이 아니면 반복
        if num % 2 == 0: # 짝수라면
            num = num // 2 # 2로 나누기
            answer += 1 # 횟수 +1
        else: # 홀수라면
            num = (num * 3) + 1 # 3을 곱하고 1 더하기
            answer += 1 # 횟수 +1
        if answer == 500: # 횟수가 500이 됐다면
            answer = -1 # 결과값은 -1
            break
    return answer

# 입출력 예시
num = 626331
print(solution(num))