def solution(array):
    array = sorted(array)
    answer = array[len(array) // 2]
    return answer


print(solution([9, -1, 0]))