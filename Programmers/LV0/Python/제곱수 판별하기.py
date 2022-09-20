def solution(n):
    answer = 2
    i = 1
    while True:
        res = i * i
        if res > n:
            break
        elif res == n:
            answer = 1
        i += 1
    return answer


n = 976
print(solution(n))