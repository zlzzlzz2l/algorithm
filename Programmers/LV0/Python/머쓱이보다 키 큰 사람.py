def solution(array, height):
    answer = 0
    for h in array:
        if h > height:
            answer += 1
    return answer


array = [180, 120, 140]
height = 190

print(solution(array, height))