def solution(my_string):
    answer = ''
    for s in my_string:
        if s.islower():
            answer += s.upper()
        else:
            answer += s.lower()
    return answer


my_string = "cccCCC"
print(solution(my_string))