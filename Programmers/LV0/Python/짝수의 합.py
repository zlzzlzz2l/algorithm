def solution(n):
    res_list = [i for i in range(1, n+1) if i % 2 == 0]
    return sum(res_list)


print(solution(10))