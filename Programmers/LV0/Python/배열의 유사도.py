def solution(s1, s2):
    answer = 0
    if len(s1) > len(s2):
        big = s1
        small = s2
    else:
        big = s2
        small = s1

    for b in big:
        for s in small:
            if b == s:
                answer += 1

    return answer


s1 = ["a", "b", "c"]
s2 = ["com", "b", "d", "p", "c"]
print(solution(s1, s2))