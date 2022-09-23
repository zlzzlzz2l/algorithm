def solution(n, t):
    answer = n
    for i in range(1, t+1):
        answer *= 2
    return answer


n = 7
t = 15
print(solution(n, t))