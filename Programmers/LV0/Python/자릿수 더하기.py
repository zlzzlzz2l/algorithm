def solution(n):
    answer = 0
    str_int = list(str(n))
    for i in str_int:
        answer += int(i)
    return answer


print(solution(1234))