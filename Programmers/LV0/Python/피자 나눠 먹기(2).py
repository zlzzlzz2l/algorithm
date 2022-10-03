def solution(n):
    answer = 0
    pizza = 6
    while True:
        if pizza % n == 0:
            answer += 1
            break
        else:
            answer += 1
            pizza += 6
    return answer


n = 4
print(solution(n))