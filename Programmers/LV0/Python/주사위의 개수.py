def solution(box, n):
    answer = 1
    for b in box:
        answer *= b // n
    return answer


box = [1, 1, 1]
n = 1
print(solution(box, n))