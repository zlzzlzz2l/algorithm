def solution(num_list, n):
    answer = []
    for i in range(len(num_list) // n):
        answer.append(num_list[n * i : n * (i + 1)])
    return answer


num_list = [100, 95, 2, 4, 5, 6, 18, 33, 948]
n = 3
print(solution(num_list, n))