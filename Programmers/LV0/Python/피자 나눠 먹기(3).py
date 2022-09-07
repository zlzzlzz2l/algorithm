def solution(slice, n):
    answer = 0
    for _ in range(n, 0, -slice):
        answer += 1
    return answer


slice = 4
n = 12
print(solution(slice, n))