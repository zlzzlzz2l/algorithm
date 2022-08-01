def solution(num_list):
    answer = [0, 0]
    for n in num_list:
        if n % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    return answer

print(solution([1, 2, 3, 4, 5]))