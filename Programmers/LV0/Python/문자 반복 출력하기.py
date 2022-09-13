def solution(my_string, n):
    answer = ''
    for s in my_string:
        answer += (s*n)
    return answer


my_string = "hello"
n = 3
print(solution(my_string, n))