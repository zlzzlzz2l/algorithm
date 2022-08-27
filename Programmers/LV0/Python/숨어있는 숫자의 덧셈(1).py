def solution(my_string):
    answer = 0
    for s in my_string:
        if s.isdigit():
            answer += int(s)
    return answer


print(solution("1a2b3c4d123"))