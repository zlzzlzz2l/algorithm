def solution(my_string):
    answer = []
    for s in my_string:
        if s.isdigit():
            answer.append(int(s))
        else:
            continue
    return sorted(answer)


print(solution("abcde0"))