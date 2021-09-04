def solution(n):
    answer = 0
    for i in range(2, n): # 2부터 n까지 반복
        if n % i == 1: # n을 i로 나눴을 때 나머지가 1이라면
            answer = i
            break # i가 가장 작은 값이므로 for문 나온다.
        else: # 아니라면
            continue # 반복
    return answer

# 입출력 예시
n = 12
print(solution(n))