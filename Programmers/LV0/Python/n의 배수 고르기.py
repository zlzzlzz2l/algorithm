def solution(n, numlist):
    answer = []
    for num in numlist:
        if num % n == 0:
            answer.append(num)
        else:
            continue
    return answer


print(solution(12, [2, 100, 120, 600, 12, 12]))