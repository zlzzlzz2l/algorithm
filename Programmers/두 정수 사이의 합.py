def solution(a, b):
    answer = 0
    if a < b: # a가 b보다 작다면
        for i in range(a, b+1): # a와 b 사이의 합
            answer += i
    elif a > b: # a가 b보다 크다면
        for i in range(a, b-1, -1):
            answer += i
    else: # a와 b가 같다면
        answer = a
    return answer

# 입출력 예시
a = 3
b = 3
print(solution(a, b))