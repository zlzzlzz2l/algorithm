def solution(n):
    answer = 0
    for _ in range(n, 0, -7):
        answer += 1
    return answer


print(solution(15))