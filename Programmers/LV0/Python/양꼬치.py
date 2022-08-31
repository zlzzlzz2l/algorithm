def solution(n, k):
    answer = 0
    answer += 12000 * n
    if n >= 10:
        bonus = n // 10
        k -= bonus
    answer += 2000 * k
    return answer


print(solution(10, 3))