def solution(array):
    answer = []
    num = max(array)
    idx = array.index(num)
    answer.append(num)
    answer.append(idx)
    return answer


print(solution([9, 10, 11, 8]))