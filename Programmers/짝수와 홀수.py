def solution(num):
    answer = ''
    if num % 2 == 0: # 입력값을 2로 나누었을 때 나머지가 0이면 짝수
        answer = "Even"
    else: # 나머지가 1이면 홀수
        answer = "Odd"
    return answer

# 입출력 예시
num = 3
print(solution(num))