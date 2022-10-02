def solution(num, k):
    num, k = str(num), str(k)
    if k in num:
        answer = num.index(k) + 1
    else:
        answer = -1
    return answer


num = 29183
k = 1
print(solution(num, k))