def solution(hp):
    answer = 0
    res = 1
    while hp != 0:
        if hp >= 5:
            res = hp // 5
            hp %= 5
            answer += res
        if hp >= 3:
            res = hp // 3
            hp %= 3
            answer += res
        if hp >= 1:
            res = hp // 1
            hp %= 1
            answer += res

    return answer


hp = 999
print(solution(hp))