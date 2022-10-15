def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        res = [1, ]
        for j in range(2, i+1):
            if i % j == 0:
                res.append(j)
        if len(res) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer


left = 13
right = 17
print(solution(left, right))