def solution(num_list):
    answer = []
    for n in range(len(num_list)-1, -1, -1):
        answer.append(num_list[n])
    return answer


num_list = [1, 1, 1, 1, 1, 2]
print(solution(num_list))